import app
from datapoints import create
from users import create as user_create
import pandas as pd
def graph():
    pass


def menu():
    print('\033[35m'
          '1. Create Datapoint\n'
          '2. Display Graph\n'
          '3. Make User\n')

    user_selection = input('Select Option: ')
    # This is where we would put an error handler for user_selection
    if user_selection == '1':
        create(app.DataPoint)
    elif user_selection == '2':
        # graph()
        print("Lol")
    elif user_selection == '3':
        user = {'last_name':'Bethla', 'first_name':'Lucus','datapoints':[]}
        user_create(user)

menu()

