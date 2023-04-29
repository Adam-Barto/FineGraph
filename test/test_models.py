import json
from unittest import TestCase
import users
import datapoints
import pandas as pd
from config import app, basedir, db
from models import User, DataPoint, TypeOfPayment_Dict, TypeOfCategory_Dict


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
            users.delete(new_user[0].get('id')) # Clean up after itself.

    def test_datapoint_creation(self):
        setup_test_database()
        with app.app_context():
            db.create_all()
            payment_type = TypeOfPayment_Dict.get(1)
            payment_from = "1234"
            amount = "123.45"
            date = "02-03-2009"
            category = TypeOfCategory_Dict.get(1)
            test_datapoint = json.loads(
                '{' + f'"user_id": "1",'
                      f' "payment_type": "{payment_type}",'
                      f' "payment_from": "{payment_from}",'
                      f' "amount": "{amount}",'
                      f' "date": "{date}",'
                      f' "category": "{category}"' + '}'
            )
            new_datapoint = datapoints.create(test_datapoint)
            actual = datapoints.read_data(new_datapoint[0].get('id')).get('payment_type')
            expected = 'Check'
            self.assertEqual(expected, actual)
            datapoints.delete(new_datapoint[0].get('id')) # Clean up after itself.

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
