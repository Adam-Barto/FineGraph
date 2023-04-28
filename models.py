from enum import Enum
from datetime import datetime
from marshmallow_sqlalchemy import fields
from config import db, ma


class TypeOfPayment(Enum):
    CHECK = 1,
    VISA = 2,
    MASTERCARD = 3,

    OTHER = 0  # When the person does not fill it out.


class TypeOfCategory(Enum):
    FOOD = 1,
    HEALTH = 2,
    EDUCATION = 3,
    ENTERTAINMENT = 4,
    CHARITY = 5,

    OTHER = 0  # When the person does not fill it out.


class DataPoint(db.Model):
    __tablename__ = "datapoint"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    # The type of payment method used.
    payment_type = db.Column(db.Enum, primary_key=True)
    # Can be last digits of the card or a check number
    payment_from = db.Column(db.Integer, primary_key=True)

    # Amount Paid
    amount = db.Column(db.Float, primary_key=True)

    # Time of Payment
    date = db.Column(db.DateTime)

    # Category of Payment
    category = db.Column(db.Enum)


class DataSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DataPoint
        load_instance = True
        sqla_session = db.session
        include_fk = True


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(32), nullable=False)
    first_name = db.Column(db.String(32))

    datapoints = db.relationship(
        DataPoint,
        backref="user",
        cascade="all, delete, delete-orphan",
        single_parent=True
    )


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session
        include_relationships = True

    datapoints = fields.Nested(DataSchema, many=True)


database_schema = DataSchema()
user_schema = UserSchema()
users_schema = UserSchema(many=True)
