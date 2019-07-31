from flask import Flask
from core.database import init_db
import os
import logging

def create_app():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.urandom(24)

    app.config.from_object('config.config.Config')

    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    logging.getLogger('sqlalchemy.orm.unitofwork').setLevel(logging.DEBUG)

    init_db(app)

    return app

app = create_app()
