#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine

engine = create_engine('mysql://root:jeesetfa@localhost/MarsGeo?charset=utf8')
connection = engine.connect()
result = connection.execute("select * from  min_res")
for row in result:
    print "name:", row['name'], "description", row['description']
connection.close()