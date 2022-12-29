from flask import Flask, request, jsonify, render_template, redirect, flash, Response
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, Cupcake
from forms import CupcakeForm
import pdb
import random


app = Flask(__name__)
test_app = Flask(__name__)



app.config['SECRET_KEY'] = "farts"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/donuts'
app.config['SQLALCHEMY_BINDS'] = {'testDB': 'sqlite:///test_donuts.db'}

app.debug = False
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPTS_REDIRECTS'] = False

connect_db(app)
app.app_context().push()


@app.route('/')
def index():
    return redirect('/main')


@app.route('/main')
def main_page():
    return render_template('home.html')

@app.route('/add', methods=['GET','POST'])
def add_with_JS():
    form = CupcakeForm()
    return render_template('add.html', form=form) 

@app.route('/api/cupcakes')
def show_all_cupcakes():
    cakes = [cake.serialize() for cake in Cupcake.query.all()]
    return jsonify(cakes=cakes)


@app.route('/api/cupcakes/<int:cake_id>')
def show_single_cupcake(cake_id):
    cake = Cupcake.query.get_or_404(cake_id)
    return jsonify(cake=cake.serialize())


@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    new_cake = Cupcake(
        flavor=request.json['flavor'],
        rating=request.json['rating'],
        size=request.json['size'],
        image=request.json['image']
    )
    if not new_cake.image:
        new_cake.image = random.choice(Cupcake.pics)

    db.session.add(new_cake)
    db.session.commit()

    return (jsonify(new_cake=new_cake.serialize()), 201)

@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    
    cupcake = Cupcake.query.get_or_404(id)
    
    cupcake.flavor = request.json['flavor']
    cupcake.rating = request.json['rating']
    cupcake.size = request.json['size']
    cupcake.image = request.json['image']
    if not cupcake.image:
        cupcake.image = Cupcake.DEFAULT
        
    db.session.add(cupcake)
    db.session.commit()

    return ((jsonify(cupcake=cupcake.serialize())), 201)

@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    
    cupcake = Cupcake.query.get_or_404(id)
    
    db.session.delete(cupcake)
    db.session.commit()
    
    return(jsonify(message = f"Successfully deleted the {cupcake.flavor} donut"))

