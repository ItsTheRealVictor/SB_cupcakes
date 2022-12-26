from flask import Flask, request, jsonify, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, Cupcake
app = Flask(__name__)

app.config['SECRET_KEY'] = "farts"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/donuts'
app.config['SQLALCHEMY_BINDS'] = {'testDB' : 'sqlite:///test_donuts.db'}

app.debug = True
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPTS_REDIRECTS'] = False 

connect_db(app)
app.app_context().push()

@app.route('/')
def index():
    return redirect('/main')
@app.route('/main')
def main_page():
    return render_template('/home.html')

@app.route('/api/cupcakes')
def show_all_cupcakes():
    cakes = [cake.serialize() for cake in Cupcake.query.all()]
    return jsonify(cakes=cakes)


@app.route('/api/cupcakes/<int:cake_id>')
def show_single_cupcake(cake_id):
    cake = Cupcake.query.get_or_404(cake_id)
    return jsonify(cake=cake.serialize())