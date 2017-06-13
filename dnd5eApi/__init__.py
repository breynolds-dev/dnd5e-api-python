import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={"*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CORS_HEADERS'] = 'Content-Type'



db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app, prefix="/v1")

import dnd5eApi.routes.endpoints
#
# db.reflect()
# db.drop_all()
#
# db.create_all()
# db.session.commit()
#
# import seed_db
