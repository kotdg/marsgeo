from marsgeo import app
from flask import render_template, session
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base


engine = create_engine("mysql://root:jeesetfa@localhost/MarsGeo?charset=utf8")
Base = automap_base()
Base.prepare(engine, reflect=True)
MinResurs = Base.classes.min_res
Minerals = Base.classes.mineral
Rocks = Base.classes.rock
Methods = Base.classes.method
MethodsRock = Base.classes.method_rock
Min_min_res = Base.classes.min_min_res
Rock_min = Base.classes.rock_min


session = Session(engine)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/min_res')
def min_res():
    min_res_list = session.query(MinResurs.id, MinResurs.name, MinResurs.formula, MinResurs.note).order_by(MinResurs.name)
    return render_template('min_res.html', min_res_list=min_res_list)

@app.route('/min_res/<int:id>', methods=['GET'])
def min_res_id(id):
    min_res = session.query(MinResurs.name, MinResurs.formula, MinResurs.id, MinResurs.description, MinResurs.pic).filter(MinResurs.id == id)
    rocks = session.query(Rocks.name, Rocks.id).filter(Rock_min.id_rock == Rocks.id).filter(Rock_min.id_mineral == Minerals.id).filter(Min_min_res.id_mineral == Minerals.id).filter(Min_min_res.id_min_res == MinResurs.id).filter(MinResurs.id == id).all()
    return render_template('min_res_id.html', min_res=min_res, rocks=rocks)

@app.route('/mineral')
def mineral():
    mineral_list = session.query(Minerals.name, Minerals.id, Minerals.description, Minerals.formula, Minerals.pic).order_by(Minerals.name)
    return render_template('mineral.html', mineral_list=mineral_list)

@app.route('/mineral/<int:id>', methods=['GET'])
def mineral_id(id):
    mineral = session.query(Minerals.name, Minerals.id, Minerals.description, Minerals.pic).filter(Minerals.id == id)
    return render_template('mineral_id.html', mineral=mineral)

@app.route('/rock')
def rock():
    rock_list = session.query(Rocks.name, Rocks.id, Rocks.description, Rocks.pic).order_by(Rocks.name)
    return render_template('rock.html', rock_list=rock_list)

@app.route('/rock/<int:id>', methods=['GET'])
def rock_id(id):
    rock = session.query(Rocks.name, Rocks.id, Rocks.description, Rocks.pic).filter(Rocks.id == id)
    methods_rock = session.query(MethodsRock.id, MethodsRock.value, Methods.name).filter(Methods.id == MethodsRock.id_method).filter(MethodsRock.id_rock == id)
    return render_template('rock_id.html', rock=rock, methods_rock=methods_rock)


@app.route('/method')
def method():
    method_list = session.query(Methods.id, Methods.name, Methods.description).order_by(Methods.name)
    return render_template('method.html', method_list=method_list)


@app.route('/method/<int:id>', methods=['GET'])
def method_id(id):
    method = session.query(Methods.id, Methods.name, Methods.description, Methods.pic).filter(Methods.id == id)
    rocks = session.query(Rocks.name, Rocks.id).filter(MethodsRock.id_rock == Rocks.id).filter(MethodsRock.value > 60).filter(MethodsRock.id_method == id).order_by(Rocks.name).all()
    return render_template('method_id.html', method=method, rocks=rocks)


@app.route('/article')
def article():
    return render_template('article.html')


session.close()





