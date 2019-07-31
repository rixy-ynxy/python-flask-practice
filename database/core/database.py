from flask_sqlalchemy import SQLALchemy
from flask_migrate import Migrate

db = SQLALchemy()

def init_db(app):
    db.init_app(app)
    Migrate(app, db)

