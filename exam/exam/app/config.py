import os

SECRET_KEY = '123456qwerty'
SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://std_2248_exam:12345678@std-mysql.ist.mospolytech.ru/std_2248_exam'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = False
USER_ROLE_IO = 1
MODER_ROLE_ID = 2
ADMIN_ROLE_ID = 3

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media', 'images')
