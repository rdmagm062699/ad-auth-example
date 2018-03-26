from flask import Blueprint, redirect, url_for, session, request, render_template, flash
from flask_login import login_required, current_user
from app.b2c_mgmt.forms import CreateUserForm
from app.b2c_mgmt.user_operations import UserOperations
from app.b2c_mgmt.transformers.transformers import Transformers
from app import app, config, login_manager
import types

mod_b2c_mgmt = Blueprint('b2c_mgmt', __name__, url_prefix='/b2c_mgmt')

@mod_b2c_mgmt.route('/my_caregivers')
@login_required
def my_caregivers():
    persons = Transformers().transform(UserOperations(config).users())
    return render_template('list_users.html', persons=persons, attributes=config['iam_user_attributes'].split(','), list=list, isinstance=isinstance)

@mod_b2c_mgmt.route('/add_user', methods=['GET', 'POST'])
@login_required
def add_user():
    form = CreateUserForm(request.form)
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        franchise_number = form.franchise_number.data
        flash('You entered %s' % { 'first_name': first_name, 'last_name': last_name, 'email': email, 'franchise_number': franchise_number })
        return redirect(url_for('b2c_mgmt.add_user'))
    return render_template('create_user.html', form=form)
