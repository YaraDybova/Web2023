from flask import Blueprint, redirect, render_template, request, url_for, flash, abort, send_from_directory
from flask_login import current_user, login_required
from sqlalchemy import desc
from app import db
import os
import bleach
import markdown
from auth import check_rights

bp = Blueprint('book', __name__, url_prefix='/book')

from models import Genre, Book, Book_Genre, Cover, Review
from tools import ImageSaver

PER_PAGE = 10


@bp.route('/new', methods=['GET', 'POST'])
@check_rights('new')
def new():
    if request.method == 'GET':
        genres = Genre.query.all()
        return render_template('book/new.html', genres=genres)
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        publisher = request.form.get('publisher')
        amount = request.form.get('amount')
        year = request.form.get('year')
        description = bleach.clean(request.form.get('description'))
        file = request.files.get('cover_img')
        cover = ImageSaver(file).save()
        book = Book(title=title, description=description, year=year, publisher=publisher, author=author, pages=amount, cover_id=cover.id)
        db.session.add(book)
        db.session.commit()
        genres = request.form.getlist('genre_id')
        for i in genres:
            genre_in_db = Book_Genre(books_id=book.id, genres_id=i)
            db.session.add(genre_in_db)
            db.session.commit()
        flash(f'Книга "{book.title}" успешно добавлена!', 'success')
        return redirect(url_for('index'))


@bp.route('/<int:book_id>/edit', methods=['GET', 'POST'])
@check_rights('edit')
def edit(book_id):
    book = Book.query.get(book_id)
    genres = Genre.query.all()
    if request.method == 'GET':
        selected_genres = Book_Genre.query.filter_by(books_id=book_id).all()
        selected_genres_list = []
        for i in selected_genres:
            selected_genres_list.append(i.genres_id)
        return render_template('book/edit.html', book=book, genres=genres, selected_genres_list=selected_genres_list)
    if request.method == 'POST':
        book.title = request.form.get('title')
        book.author = request.form.get('author')
        book.publisher = request.form.get('publisher')
        book.amount = request.form.get('amount')
        book.year = request.form.get('year')
        book.description = bleach.clean(request.form.get('description'))
        db.session.commit()
        while Book_Genre.query.filter_by(books_id=book_id).first():
            db.session.delete(Book_Genre.query.filter_by(books_id=book_id).first())
            db.session.commit()
        selected_genres = request.form.getlist('genre_id')
        for i in selected_genres:
            a = Book_Genre(books_id=book_id, genres_id=i)
            db.session.add(a)
            db.session.commit()
        flash(f'Книга "{book.title}" успешно изменена!', 'success')
        return redirect(url_for('index'))


@bp.route('/show/<int:book_id>')
def show(book_id):
    book = Book.query.get(book_id)
    book.description = markdown.markdown(book.description)
    book_genre = Book_Genre.query.all()
    cover = Cover.query.filter_by(id=book.cover_id).first()
    img = cover.url
    if current_user.is_authenticated:
        review = Review.query.filter_by(user_id=current_user.id, book_id=book_id, review_status_id=2).first()
        if review:
            review.text = markdown.markdown(review.text)
        other_reviews = Review.query.filter(Review.user_id != current_user.id)\
            .filter_by(book_id=book_id, review_status_id=2).all()
    else:
        review = False
        other_reviews = Review.query.filter_by(book_id=book_id, review_status_id=2).all()
    for other_review in other_reviews:
        other_review.text = markdown.markdown(other_review.text)
    return render_template('book/show.html', book=book, book_genre=book_genre, img=img, review=review,
                           other_reviews=other_reviews)


@bp.route('/my-reviews')
@login_required
@check_rights('watch_my_reviews')
def my_reviews():
    my_reviews = Review.query.filter_by(user_id=current_user.id).all()
    for my_review in my_reviews:
        my_review.text = markdown.markdown(my_review.text)

    return render_template('book/my_reviews.html', reviews=my_reviews)


@bp.route('/moderation/reviews', methods=['GET'])
@login_required
@check_rights('edit')
def moderation_reviews():
    page = request.args.get('page', 1, type=int)
    pagination = Review.query.filter_by(review_status_id=1)\
        .order_by(desc(Review.created_at))\
        .paginate(page=page, per_page=PER_PAGE)
    reviews = pagination.items

    return render_template('book/moderation_reviews.html', reviews=reviews, pagination=pagination)


@bp.route('/moderation/reviews/<int:review_id>', methods=['GET', 'POST'])
@login_required
@check_rights('edit')
def moderation_show_review(review_id):
    review = Review.query.filter_by(review_status_id=1, id=review_id).first()
    if review is None:
        flash(f'Рецензия не найдена!', 'danger')
        return redirect(url_for('book.moderation_reviews'))

    review.text = markdown.markdown(review.text)
    if request.method == 'GET':
        return render_template('book/moderation_review.html', review=review)

    confirm = request.form.get('confirm')
    if confirm != 'reject' and confirm != 'confirm':
        flash(f'Неверно передан параметр confirm!', 'danger')
        return redirect(url_for('book.moderation_show_review', review_id=review_id))
    if confirm == 'confirm':
        review.review_status_id = 2
    else:
        review.review_status_id = 3
    db.session.commit()

    return redirect(url_for('book.moderation_reviews'))


@bp.route('/delete/<int:book_id>', methods=['POST'])
@check_rights('delete')
def delete(book_id):
    if request.method == 'POST':
        try:
            book = Book.query.filter_by(id=book_id).first()
            img = Cover.query.filter_by(id=book.cover_id).first()
            db.session.delete(book)
            db.session.delete(img)
            db.session.commit()
            img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media', 'images', img.storage_filename)
            os.remove(img_path)
            flash(f'Книга успешно удалена!', 'success')
        except Exception as e:
            flash(f'Ошибка удаления книги! ' + str(e), 'danger')
        return redirect(url_for('index'))


@bp.route('/review/<int:book_id>', methods=['GET', 'POST'])
@login_required
def review(book_id):
    book = Book.query.get(book_id)
    if request.method == 'POST':
        text = request.form.get('review')
        mark = int(request.form.get('mark'))
        review = Review(rating=mark, text=text, book_id=book_id, user_id=current_user.get_id(), review_status_id=1)
        book.rating_num += 1
        book.rating_sum += int(review.rating)
        db.session.add(review)
        db.session.commit()
        flash(f'Отзыв был успешно добавлен!', 'success')
        return redirect(url_for('book.show', book_id=book.id))
    if request.method == 'GET':
        return render_template('book/review.html', book=book)