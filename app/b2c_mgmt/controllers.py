from flask import Blueprint, redirect, url_for, session, request, render_template
from flask_login import login_required, current_user
from app.b2c_mgmt.user_operations import b2c_users
from app import app, config, login_manager

mod_b2c_mgmt = Blueprint('b2c_mgmt', __name__, url_prefix='/b2c_mgmt')

@mod_b2c_mgmt.route('/my_caregivers')
@login_required
def my_caregivers():
    return render_template('list_b2c.html', list=b2c_users(config))
