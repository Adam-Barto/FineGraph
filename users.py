import json

from flask import abort, make_response

from config import db
from models import User, users_schema, user_schema

def read_all():
    user = User.query.all()
    return users_schema.dump(user)


def create(user):
    new_user = user_schema.load(user, session=db.session)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.dump(new_user), 201


def read_one(user_id):
    user = User.query.get(user_id)

    if user is not None:
        return user_schema.dump(user)
    else:
        abort(404, f"User with Id {user_id} not found")


def update(user_id, user):
    existing_user = User.query.get(user_id)

    if existing_user:
        update_user = user_schema.load(user, session=db.session)
        existing_user.first_name = update_user.first_name
        existing_user.last_name = update_user.last_name

        db.session.merge(existing_user)
        db.session.commit()
        return user_schema.dump(existing_user), 201
    else:
        abort(404, f"User with Id {user_id} not found")


def delete(user_id):
    existing_user = User.query.get(user_id)

    if existing_user:
        db.session.delete(existing_user)
        db.session.commit()
        return make_response(f"{user_id} successfully deleted", 200)
    else:
        abort(404, f"User with Id {user_id} not found")
