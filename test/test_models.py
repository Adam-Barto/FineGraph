import json
from unittest import TestCase
import users
import datapoints
import pandas as pd
from config import app, basedir, db
from models import User, DataPoint


def setup_test_database():
    app.config.update(
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{basedir}/test/testdata.db'",
    )


class Test(TestCase):

    def test_user_creation(self):
        setup_test_database()
        with app.app_context():
            db.create_all()
            last_name = "Test"
            first_name = "User"
            test_user = json.loads('{'+f'"last_name": "{last_name}", "first_name": "{first_name}", "datapoints": []'+'}'
                                   )
            new_user = users.create(test_user)
            actual = users.read_one(new_user[0].get('id')).get('last_name')
            expected = 'Test'
            self.assertEqual(expected, actual)
            users.delete(new_user[0].get('id'))

    def test_datapoint_creation(self):
        setup_test_database()
        with app.app_context():
            db.create_all()
            payment_type = 'Visa'
            payment_from = '1234'
            amount = '123.45'
            date = '02-03-2009'
            category = 'Food'
            test_datapoints = json.loads(
                '{' + f'"payment_type": {payment_type}, "payment_from": {payment_from}, "amount": {amount}, "date": {date}, "category": {category}' + '}'
            )
            datapoint_count = pd.DataFrame(datapoints.read_data()).id.count()
            expected = datapoint_count + 1
            users.create(test_datapoints)
            actual = pd.DataFrame(datapoints.read_all()).id.count()
            self.assertEqual(expected, actual)

    def test_print_dataset(self):
        setup_test_database()
        with app.app_context():
            db.create_all()
            df = pd.DataFrame(users.read_all())
            print(df)
            # df.drop_duplicates(subset='last_name')
            # db.drop_all()

    def test_delete_database(self):
        setup_test_database()
        with app.app_context():
            db.drop_all()

    def test_data_base(self):
        self.fail()

    def test_user_schema(self):
        self.fail()
