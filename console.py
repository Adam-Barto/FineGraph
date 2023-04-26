import pathlib
import sqlite3

import models
from datapoints import create
import pandas as pd
basedir = pathlib.Path(__file__).parent.resolve().parent

# Makes the Database if it doesn't exist, or connects to it.
# db = sqlite3.connect(f"{basedir / 'dataset.db'}")
# sql = '''
#           CREATE TABLE IF NOT EXISTS datapoints (
#           payment_type TEXT NOT NULL,
#           payment_from INTEGER NOT NULL,
#           amount FLOAT NOT NULL,
#           date TEXT NOT NULL,
#           category INTEGER NOT NULL
#           );
#         '''
# db.execute(sql)
def graph():
    pass


def menu():
    print('\033[35m'
          '1. Create Datapoint\n'
          '2. Display Graph\n')
    user_selection = input('Select Option: ')
    # This is where we would put an error handler for user_selection
    if user_selection == '1':
        create(models.DataPoint)
    elif user_selection == '2':
        # graph()
        print(pd.read_sql("SELECT * FROM datapoints", db))


menu()
