import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))

db = SQLAlchemy()

"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""


def setup_db(app, database_filename=database_filename):
    database_path = "sqlite:///{}".format(
        os.path.join(project_dir, database_filename)
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True

    db.app = app
    db.init_app(app)
    db.create_all()

    Migrate(app, db)


"""
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple
    verisons of a database
"""


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
