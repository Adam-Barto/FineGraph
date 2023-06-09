from flask import render_template, current_app
from config import app, setup

from models import User, DataPoint

console_test = False


@app.route("/")
def home():
    # user = User.query.all()  # Maybe see about only exporting the user you care about?
    return render_template("baseline.html")  # Start it up.


# @app.route("/Graph")
# def graph():
#     datapoints = DataPoint.query.all()
#     return render_template("graph.html", datapoints=datapoints)
def activate():
    if console_test:
        setup()
    else:
        app.run(host="0.0.0.0", port=8000, debug=True)


if __name__ == "__main__":
    activate()
