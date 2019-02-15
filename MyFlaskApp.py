from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

class OrderForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    email = StringField('St. Andrews Email Address:', validators=[DataRequired()])
    type = SelectField('Type:', choices=[('delivery', 'Delivery'), ('pickup', 'Pick Up')], validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    order = OrderForm()
    return render_template('index.html', form=order)

@app.route('/info')
def info():
    return '<p>This page provides info about my application</p>'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
