import json
from unittest import TestCase
import users
import datapoints
import pandas as pd
from config import app, basedir, db
from models import User, DataPoint


def setup_test_database():
    app.config.update(
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{basedir / 'testdata.db'}",
    )


class Test(TestCase):

    def test_user_creation(self):
        setup_test_database()
        with app.app_context():
            db.create_all()
            last_name = "Test"
            first_name = "User"
            actual = json.loads('{'+f'"last_name": "{last_name}", "first_name": "{first_name}", "datapoints": []'+'}'
                                )
            print(actual)
            users.create(actual)
            expected = pd.DataFrame(users.read_all())
            print(expected)
            self.assertEqual(expected, actual)

    def test_type_of_category(self):
        self.fail()

    def test_data_point(self):
        self.fail()

    def test_user(self):
        self.fail()

    def test_data_base(self):
        self.fail()

    def test_user_schema(self):
        self.fail()
