import json
from datapoints import create
from users import create as user_create


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
        datapoints = '{}'
        datapoints = json.loads(datapoints)
        create(datapoints)
    elif user_selection == '2':
        # graph()
        print("graph code")
    elif user_selection == '3':
        user = '{"last_name": "Bethla", "first_name": "Lucus", "datapoints": []}'
        user = json.loads(user)
        print(user)
        user_create(user)


# menu()
