from flask import Flask


def create_flask_app(config):
    flask_app = Flask(__name__)
    flask_app.config.from_object(config)

    flask_app.app_context().push()

    return flask_app
