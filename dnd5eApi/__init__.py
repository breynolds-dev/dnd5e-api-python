import os

from flask import Flask, jsonify
from flask_restful import Resource, Api, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask( __name__ )

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy( app )

api = Api( app )

import dnd5eApi.routes.endpoints

# db.reflect()
# db.drop_all()

# # create the database and the database table
# db.create_all()
# db.session.commit()

# import seed_db
