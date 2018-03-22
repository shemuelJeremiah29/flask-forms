from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, validators, RadioField, SubmitField 
from wtforms.validators import DataRequired, Email
import datetime 

class MyProfileForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    location = StringField('Location', validators=[DataRequired()]) 
    gender= RadioField('Gender', choices=[('Male', 'male'), ('Female','female')])
    biography= TextAreaField('Biography', [validators.Length( min=50, max=500)]) 
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])  
    created_on= datetime.datetime.now  
    submit=SubmitField(label='Submit')