from flask import abort, make_response
from config import db
from models import DataPoint, database_schema, User


def read_data(datapoint_id):
    datapoint = DataPoint.query.get(datapoint_id)

    if datapoint is not None:
        return database_schema.dump(datapoint)
    else:
        abort(404, f"Datapoint with ID {datapoint_id} not found")


def update(datapoint_id, datapoint):
    existing_datapoint = DataPoint.query.get(datapoint_id)

    if existing_datapoint:
        update_datapoint = database_schema.load(datapoint, session=db.session)
        existing_datapoint.amount = update_datapoint.amount
        existing_datapoint.payment_type = update_datapoint.payment_type
        existing_datapoint.payment_from = update_datapoint.payment_from
        existing_datapoint.category = update_datapoint.category
        db.session.merge(existing_datapoint)
        db.session.commit()
        return database_schema.dump(existing_datapoint), 201
    else:
        abort(404, f"Datapoint with ID {datapoint_id} not found")


def delete(datapoint_id):
    existing_datapoint = DataPoint.query.get(datapoint_id)

    if existing_datapoint:
        db.session.delete(existing_datapoint)
        db.session.commit()
        return make_response(f"{datapoint_id} successfully deleted", 204)
    else:
        abort(404, f"Datapoint with ID {datapoint_id} not found")


def create(datapoint):
    user_id = datapoint.get("user_id")
    user = User.query.get(user_id)
    if user:
        new_datapoint = database_schema.load(datapoint, session=db.session)
        user.datapoints.append(new_datapoint)
        db.session.commit()
        return database_schema.dump(new_datapoint), 201
    else:
        abort(404, f"User not found for ID: {user_id}")
