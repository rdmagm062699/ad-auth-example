from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import Required, NumberRange, Length, Email, ValidationError
from flask_login import current_user

class CreateUserForm(FlaskForm):
    franchise_number = IntegerField('Franchise Number', [Required(message='You must enter a valid integer for a franchise number'), NumberRange(0,4000)])
    first_name = StringField('First Name', [Required(message="Please enter a first name"), Length(2)])
    last_name = StringField('Last Name', [Required(message="Please enter a last name"), Length(2)])
    email = StringField('Email', [Required(message="Please enter a valid e-mail address"), Email()])

    def validate_franchise_number(form, field):
        # As far as I can tell you can only do limited validation types for cases where you need current_user ... weird
        if not field.data in current_user.franchises():
            raise ValidationError('You may only create users that you are authorized for {}'.format(current_user.franchises()))
