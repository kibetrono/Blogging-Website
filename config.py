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

class ProdConfig(Config):
    """Production configuration child class
    Args:
    Config: The parent configuration class with General configuration settings
    """
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kibet:KibetFlask@localhost/ownblog'

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")  # or other relevant config var
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    # rest of connection code using the connection string `uri`
