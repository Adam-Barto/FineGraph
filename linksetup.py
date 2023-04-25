from app import app
from flask import render_template
from models import User, DataPoint


@app.route("/")
def home():
    user = User.query.all() # Maybe see about only exporting the user you care about?
    return render_template("home.html", user=user)

@app.route("/Graph")
def graph():
    datapoints = DataPoint.query.all()
    return render_template("graph.html", datapoints=datapoints)


