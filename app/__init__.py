from flask import Flask, render_template
from flask_login import LoginManager
import yaml

app = Flask(__name__)
app.config.from_object('config')

with open("config/config.yml", 'r') as ymlfile:
    config = yaml.load(ymlfile)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

from app.mod_auth.controllers import mod_auth as auth_module
from app.b2c_mgmt.controllers import mod_b2c_mgmt as b2c_module
app.register_blueprint(auth_module)
app.register_blueprint(b2c_module)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
