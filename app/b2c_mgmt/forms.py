from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import Required, NumberRange

class CreateFranchiseGroupForm(FlaskForm):
    franchise_number = IntegerField('Franchise Number', [Required(message='You must enter a franchise number'), NumberRange(0,4000)])
