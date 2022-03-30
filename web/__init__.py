from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = "dsfajkdfjbasfbdabcabbhcbhasdb"

    from . import web
    app.register_blueprint(web.bp)

    return app
