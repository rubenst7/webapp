class BaseConfig(object):
    DB_NAME = 'db'
    DB_USER = 'test'
    DB_PASS = 'test'
    DB_PORT = '5432'
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASS}@postgres:{DB_PORT}/{DB_NAME}'

pass
