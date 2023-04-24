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
    # Amount Paid
    amount = db.Column(db.Float, primary_key=True)

    # Time of Payment
    date = db.Column(db.DateTime)

    # The type of payment method used.
    payment_type = db.Column(db.TypeOfPayment, primary_key=True)

    # Can be last digits of the card or a check number
    payment_from = db.Column(db.Integer, primary_key=True)

    # Category of Payment
    category = db.Column(db.TypeOfCatagory)


# class DataBase(ma.SQLAlchemyAutoSchema):
#     class Meta:

