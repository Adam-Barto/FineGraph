import json
from datapoints import create, read_data
from users import create as user_create, read_all
from models import db, TypeOfPayment_Dict, TypeOfCategory_Dict
import pandas as pd


def build_datapoint():
    # id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    # The type of payment method used.
    [print(f'\033[35m {key}. {value} \033[0m') for (key, value) in TypeOfPayment_Dict.items()]
    payment_type = input('\033[35m Your Choice: \033[0m')

    # Can be last digits of the card or a check number
    payment_from = input('\033[35m First Four #\'s: \033[0m')

    # Amount Paid
    amount = input('\033[35m Amount: $\033[0m')

    # Time of Payment
    date = input('\033[35m Date: \033[0m')

    # Category of Payment
    [print(f'\033[35m {key}. {value} \033[0m') for (key, value) in TypeOfCategory_Dict.items()]
    category = input('\033[35m Your Choice: \033[0m')
    return '{'+f'"payment_type": {payment_type}, "payment_from": {payment_from}, "amount": {amount}, "date": {date}, "category": {category}'+'}'




def build_user():
    last_name = input('\033[35m Last Name: \033[0m')
    first_name = input('\033[35m First Name: \033[0m')
    return '{'+f'"last_name": "{last_name}", "first_name": "{first_name}", "datapoints": []'+'}'


def graph():
    pass


def menu():
    print('\033[35m'
          '1. Create Datapoint\n'
          '2. Display Graph\n'
          '3. Make User\n'
          '4. Display Data\n'
          '\033[0m')

    user_selection = input('Select Option: ')
    # This is where we would put an error handler for user_selection
    if user_selection == '1':
        datapoints = build_datapoint()
        datapoints = json.loads(datapoints)
        create(datapoints)
    elif user_selection == '2':
        # graph()
        lol = pd.DataFrame(read_all())
        print(read_all())  # pulled from the function file of each one.
        print(lol)
    elif user_selection == '3':
        user = build_user()# This lets us build the user, without using the Website
        print(user)
        user = json.loads(user)
        user_create(user)
    elif user_selection == '4':
        lol = pd.DataFrame(read_all())
        print(lol)

# menu()
