from decouple import config

class Config:
    SECRET_KEY='codigoFacilito'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI='mysql://root:homecast@localhost/project_login'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'sebas1999ok@gmail.com'
    MAIL_PASSWORD = config('MAIL_PASSWORD')

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI='mysql://root:homecast@localhost/sistema_covid'
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    TEST = True
config = {
    'development' : DevelopmentConfig,
    'default': DevelopmentConfig,
    'test': TestConfig
}