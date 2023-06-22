from app import db, app
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from user_policy import UserPolicy
import os
from flask import url_for


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20), nullable=False, unique=True)
    last_name = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    middle_name = db.Column(db.String(20))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id', ondelete='CASCADE'), nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<User: %r>' % self.login

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def is_user(self):
        return self.role_id == app.config.get('USER_ROLE_IO')

    @property
    def is_admin(self):
        return self.role_id == app.config.get('ADMIN_ROLE_ID')

    @property
    def is_moder(self):
        return self.role_id == app.config.get('MODER_ROLE_ID')

    def get_full_name(self):
        full_name = self.first_name
        if self.middle_name is not None:
            full_name += ' ' + self.middle_name
        if self.last_name is not None:
            full_name += ' ' + self.last_name
        return full_name

    def can(self, action):
        users_policy = UserPolicy()
        method = getattr(users_policy, action, None)
        if method is not None:
            return method()
        return False


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return '<User: %r>' % self.role_name


class Book_Genre(db.Model):
    __tablename__ = 'books_genres'
    id = db.Column(db.Integer, primary_key=True)
    books_id = db.Column(db.Integer, db.ForeignKey('books.id', ondelete='CASCADE'), nullable=False)
    genres_id = db.Column(db.Integer, db.ForeignKey('genres.id', ondelete='CASCADE'), nullable=False)

    book = db.relationship('Book')
    genre = db.relationship('Genre')


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    year = db.Column(mysql.YEAR, nullable=False)
    publisher = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    cover_id = db.Column(db.Integer, db.ForeignKey('covers.id', ondelete='CASCADE'), unique=True)
    rating_sum = db.Column(db.Integer, nullable=False, default=0)
    rating_num = db.Column(db.Integer, nullable=False, default=0)

    reviews = db.relationship('Review')

    def __repr__(self):
        return '<Book: %r>' % self.title

    @property
    def rating(self):
        if self.rating_num > 0:
            return self.rating_sum / self.rating_num
        return 0


class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String(255), nullable=False, unique=True)

    def __repr__(self):
        return '<Genre: %r>' % self.genre_name


class Cover(db.Model):
    __tablename__ = 'covers'
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(255), nullable=False)
    mime_type = db.Column(db.String(255), nullable=False)
    md5_hash = db.Column(db.String(255), nullable=False, unique=True)

    def __repr__(self):
        return '<Cover: %r>' % self.file_name

    @property
    def storage_filename(self):
        _, ext = os.path.splitext(self.file_name)
        return str(self.id) + ext

    @property
    def url(self):
        return url_for('image', cover_id=self.id)


class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id', ondelete='CASCADE'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
    rating = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=sa.sql.func.now())
    review_status_id = db.Column(db.Integer, db.ForeignKey('review_statuses.id', ondelete='CASCADE'))

    user = db.relationship('User')
    review_status = db.relationship('ReviewStatus')
    book = db.relationship('Book')

    def __repr__(self):
        return f'<Reviews: {self.user_id} {self.created_at}>'


class ReviewStatus(db.Model):
    __tablename__ = 'review_statuses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    config_name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<ReviewStatus: {self.id} {self.name} {self.config_name}>'
