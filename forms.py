from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField
from wtforms.validators import InputRequired

class CupcakeForm(FlaskForm):
    flavor = StringField('Flavor')
    rating = FloatField('Rating')
    size = StringField('Size')
    image = StringField('Image URL', default='https://tinyurl.com/demo-cupcake')