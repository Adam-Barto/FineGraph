import json
from datapoints import create, read_data
from users import create as user_create, read_all
from models import db
import pandas as pd


def graph():
    pass


def menu():
    print('\033[35m'
          '1. Create Datapoint\n'
          '2. Display Graph\n'
          '3. Make User\n'
          '\033[0m')

    user_selection = input('Select Option: ')
    # This is where we would put an error handler for user_selection
    if user_selection == '1':
        datapoints = '{}'
        datapoints = json.loads(datapoints)
        create(datapoints)
    elif user_selection == '2':
        # graph()
        lol = pd.DataFrame(read_all())
        print(read_all()) # pulled from the function file of each one.
        print(lol)
    elif user_selection == '3':
        user = '{"last_name": "Bethla", "first_name": "Lucus", "datapoints": []}'
        user = json.loads(user)
        user_create(user)


# menu()
