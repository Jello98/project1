from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, TextField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect
from flask_wtf.file import FileField, FileRequired, FileAllowed
from app import app


WTF_CSRF_SECRET_KEY='TET342525WL=2]42P[21K,10``L2@#@@$1~2`3]'

class PropertyForm(FlaskForm):

    title = TextField('title', validators=[DataRequired()])
    propertyDescription = TextAreaField('Property Description', validators=[DataRequired()])

    bedrooms = TextField('Number of Bedrooms', validators=[DataRequired()])
    bathrooms = TextField('Number of Bathrooms', validators=[DataRequired()])
    price = TextField('Price', validators=[DataRequired()])
    propertytype= SelectField('Type of Property',choices=[('Apartments', 'Apartments'),('House','House')], validators= [DataRequired()])

    location = TextField('Location', validators=[DataRequired()])
    photo= FileField('Image of Property', validators=[DataRequired()])

    submit = SubmitField("Send")