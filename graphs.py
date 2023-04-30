import pandas as pd
import matplotlib.pyplot as plt
from users import read_all
import datapoints


def graph(user_id, y_values, x_values): # This will accept the database from the user.
    df = pd.DataFrame(read_all())
    df = df.loc[df['id'] == user_id]
    index_list = ["user_id",
                  "payment_type",
                  "payment_from",
                  "amount",
                  "date",
                  "category"]
    df = pd.DataFrame(df.datapoints[0], columns=index_list)
    x_val = df.loc[df['category'] == x_values]['category']
    y_val = df.loc[df['category'] == x_values][y_values]
    plt.plot(y_val, x_val, color='red', marker='o')
    plt.title(f'{x_values} vs {y_values}', fontsize=14)
    plt.xlabel(y_values, fontsize=14)
    plt.ylabel(x_values, fontsize=14)
    plt.grid(True)
    plt.show()