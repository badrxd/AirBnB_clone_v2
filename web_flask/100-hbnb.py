#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hello_world():
    """"/hbnb: display a HTML page 100-hbnb.html"""
    states = storage.all(State)
    amenity = storage.all(Amenity)
    places = storage.all(Place)
    users = storage.all(User)
    return render_template('100-hbnb.html', states=states,
                           amenity=amenity, places=places, users=users)


@app.teardown_appcontext
def teardown_request(error):
    """remove the current SQLAlchemy Session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
