import os

SECRET_KEY = '2b0f6c24a60196f0094091f5c085d8433087e294fad6d4808ec8d881845b779a'

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://std_1929_exam:std_1929_exam@std-mysql.ist.mospolytech.ru/std_1929_exam'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media', 'images')