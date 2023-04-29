from sqlalchemy.exc import OperationalError
from datetime import datetime
from config import app, db
from models import DataPoint, User

TEST_USER = [
    {
        "last_name": "Doe",
        "first_name": "John",
        "datapoints": [
            (2, 1234, 25.90, '05-03-2022', 3),
            (1, 7456, 232.13, '01-31-2012', 4),
            (0, 2398, 123.90, '12-05-2002', 1)
        ]

    }
]


def get_data_from_table(model):
    try:
        data = db.session.query(model).all()
        db.session.close()
        return data  # formats as a list
    except OperationalError:
        return []


def create_database(db):
    db.create_all()
    for data in TEST_USER:
        new_user = User(last_name=data.get("last_name"), first_name=data.get("first_name"))
        for amount, date, payment_type, payment_from, category in data.get("datapoints", []):
            new_user.datapoints.append(
                DataPoint(
                    amount=amount,
                    date=date,
                    payment_type=payment_type,
                    payment_from=payment_from,
                    category=category
                )
            )
    db.session.commit()
    print('Created New Database')


def update_database(db, existing_user, existing_datapoints):
    db.drop_all()
    db.create_all()
    for user in existing_user:
        db.session.merge(user)
    for datapoint in existing_datapoints:
        db.session.merge(datapoint)
    db.session.commit()
    print('Updated existing Database')


with app.app_context():
    existing_user = get_data_from_table(User)
    existing_datapoints = get_data_from_table(DataPoint)

    if not existing_user:
        create_database(db)
    else:
        update_database(db, existing_user, existing_datapoints)
