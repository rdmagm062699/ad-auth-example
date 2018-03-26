from flask import Blueprint, redirect, url_for, session, request, render_template, flash
from flask_login import login_required, current_user
from app.b2c_mgmt.forms import CreateFranchiseGroupForm
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

@mod_b2c_mgmt.route('/add_franchise', methods=['GET', 'POST'])
@login_required
def add_franchise():
    form = CreateFranchiseGroupForm(request.form)
    if form.validate_on_submit():
        franchise_number = form.franchise_number.data
        print('You entered %s' % franchise_number)
        return redirect(url_for('b2c_mgmt.my_caregivers'))
    flash('My brain hurts', 'error_message')
    return render_template('create_group.html', form=form)
