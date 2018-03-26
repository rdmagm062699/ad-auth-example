from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import Required, NumberRange, Length, Email

class CreateUserForm(FlaskForm):
    franchise_number = IntegerField('Franchise Number', [Required(message='You must enter a valid integer for a franchise number'), NumberRange(0,4000)])
    first_name = StringField('First Name', [Required(message="Please enter a first name"), Length(2)])
    last_name = StringField('Last Name', [Required(message="Please enter a last name"), Length(2)])
    email = StringField('Email', [Required(message="Please enter a valid e-mail address"), Email()])
