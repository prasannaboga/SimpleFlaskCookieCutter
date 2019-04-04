import locale
from flask import Flask

from app.pages import views


def create_app(test_config=None):
    """ init app """
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_object('config')
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    app.config['BUNDLE_ERRORS'] = True

    # register blueprints
    app.register_blueprint(views.pages_bp)

    # Setting local currency
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    return app
