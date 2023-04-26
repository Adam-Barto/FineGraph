import pathlib
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

basedir = pathlib.Path(__file__).parent.resolve()
app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{basedir / 'dataset.db'}",
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)
db = SQLAlchemy(app)
ma = Marshmallow(app)

