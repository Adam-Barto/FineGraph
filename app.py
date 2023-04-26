from flask import render_template, current_app
from models import User, DataPoint
from config import app


@app.route("/")
def home():
    user = User.query.all()  # Maybe see about only exporting the user you care about?
    return render_template("home.html", user=user)


# @app.route("/Graph")
# def graph():
#     datapoints = DataPoint.query.all()
#     return render_template("graph.html", datapoints=datapoints)

# def create_app():
#     user = User
#     datapoint = DataPoint
#     with app.app_context():
#         current_app.user = User
#         current_app.datapoint = DataPoint
#     return app


if __name__ == "__main__":
    # app = create_app()
    app.run(host="0.0.0.0", port=8000, debug=True)
