from flask import Flask, render_template, request, abort, send_from_directory, session
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
application = app

app.config.from_pyfile('config.py')

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)

from auth import bp as auth_bp, init_login_manager
from book import bp as book_bp

app.register_blueprint(auth_bp)
app.register_blueprint(book_bp)

init_login_manager(app)

from models import *

PER_PAGE = 10


def search_params(title, genres_list, years_list, amount_from, amount_to, author):
    return {
        'title': title,
        'genre_id': genres_list,
        'year': years_list,
        'amount_from': amount_from,
        'amount_to': amount_to,
        'author': author
    }


@app.route('/')
def index():
    book_genre = Book_Genre.query.all()
    page = request.args.get('page', 1, type=int)
    pagination = Book.query.paginate(page=page, per_page=PER_PAGE)
    books = pagination.items
    is_found = books != []
    rating = Book.rating

    return render_template('index.html', books=books, book_genre=book_genre, pagination=pagination, rating=rating, is_found=is_found)

@app.route('/media/images/<cover_id>')
def image(cover_id):
    cover = Cover.query.get(cover_id)
    if cover is None:
        abort(404)
    return send_from_directory(app.config['UPLOAD_FOLDER'], cover.storage_filename)

