from datetime import datetime
from marshmallow_sqlalchemy import fields
from config import db, ma

TypeOfPayment_Dict = {
    0: 'Other',
    1: 'Check',
    2: 'Visa',
    3: 'MasterCard'
}
TypeOfCategory_Dict = {
    0: 'Other',
    1: 'Food',
    2: 'Health',
    3: 'Education',
    4: 'Entertainment',
    5: 'Charity'
}


class DataPoint(db.Model):
    __tablename__ = "datapoint"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    # The type of payment method used.
    payment_type = db.Column(db.VARCHAR(32), nullable=False)
    # Can be last digits of the card or a check number
    payment_from = db.Column(db.Integer, nullable=False)

    # Amount Paid
    amount = db.Column(db.Float, nullable=False)

    # Time of Payment
    date = db.Column(db.DateTime, nullable=False)

    # Category of Payment
    category = db.Column(db.VARCHAR(32), nullable=False)


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
