import os

try:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
except:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///client.db'
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False
