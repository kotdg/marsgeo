# -*- coding: utf-8 -*-

from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base


db = SQLAlchemy()


Base = automap_base()

engine = create_engine("mysql://root:jeesetfa@localhost/MarsGeo?charset=utf8")

Base.prepare(engine, reflect=True)

MinResurs = Base.classes.min_res

session = Session(engine)

session.commit()

Min_res_list = session.query(MinResurs.name, MinResurs.formula, MinResurs.description).order_by(MinResurs.name)

for name,formula, description in Min_res_list:
    print name, formula, description




