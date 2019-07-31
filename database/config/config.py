import os

class AppConfig:

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{password}@{host}/flaskdb'.format(**{
        'user': os.getenv('DB_USER', 'testuser'),
        'password': os.getenv('DB_PASSWORD', 'password'),
        'host': os.getxenv('DB_HOST', 'localhost:5432'),
        })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_POOL_TIMEOUT = 180
    SQLALCHEMY_MAX_OVERFLOW = 0

Config = AppConfig
