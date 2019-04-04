from flask import Blueprint, flash, render_template, jsonify
from flask import current_app as app

pages_bp = Blueprint('pages', __name__, url_prefix='', template_folder='templates')


@pages_bp.route('/')
@pages_bp.route('/index')
def index():
    return render_template('index.html', app_name=app.config['APP_NAME'])
