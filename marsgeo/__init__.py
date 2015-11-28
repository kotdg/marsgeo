from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData

app = Flask(__name__)

db = SQLAlchemy(app)

import marsgeo.routes



