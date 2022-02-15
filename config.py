import os


class Config:
    '''General configuration parent class'''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://kibet:KibetFlask@localhost/ownblog'
    SECRET_KEY ='FlSkPItchA@*ppL&iCA^$tio***n'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

