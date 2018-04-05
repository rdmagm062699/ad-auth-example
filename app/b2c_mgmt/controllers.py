from flask import Blueprint, redirect, url_for, session, request, render_template, flash
from flask_login import login_required, current_user
from app.b2c_mgmt.forms import CreateUserForm
from app.b2c_mgmt.user_operations import b2c_users
from app import app, config, login_manager

mod_b2c_mgmt = Blueprint('b2c_mgmt', __name__, url_prefix='/b2c_mgmt')

@mod_b2c_mgmt.route('/my_caregivers')
@login_required
def my_caregivers():
    return render_template('b2c_management/list_b2c.html', list=b2c_users(config))

@mod_b2c_mgmt.route('/add_user', methods=['GET', 'POST'])
@login_required
def add_user():
    form = CreateUserForm(request.form)
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        franchise_number = form.franchise_number.data
        create_user(first_name, last_name, email, franchise_number)
#        flash('The result is %s' % result)
        return redirect(url_for('b2c_mgmt.add_user'))
    return render_template('b2c_management/create_user.html', form=form)
