from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, TextField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect
from flask_wtf.file import FileField, FileRequired, FileAllowed
from app import app


class PropertyForm(FlaskForm):

    title = TextField('Title', validators=[DataRequired()])
    
    propertyDescription = TextAreaField('Property Description', validators=[DataRequired()])

    bedrooms = TextField('Number of Bedrooms', validators=[DataRequired()])
    bathrooms = TextField('Number of Bathrooms', validators=[DataRequired()])
    price = TextField('Price', validators=[DataRequired()])
    propertytype= SelectField('Type of Property',choices=[('Apartments', 'Apartments'),('House','House')], validators= [DataRequired()])

    location = TextField('Location', validators=[DataRequired()])
    photo= FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg','png','jpeg'],'Only images allowed')])

    submit = SubmitField("Send")