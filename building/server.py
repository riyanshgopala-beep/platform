import os
from flask import Flask
from .router import register_routes

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def create_building():
    app = Flask(
        __name__,
        template_folder=os.path.join(BASE_DIR, "layout"),  # <-- important
        static_folder=os.path.join(BASE_DIR, "assets"),   # optional
        static_url_path="/static"
    )

    app.config["TEMPLATES_AUTO_RELOAD"] = True

    register_routes(app)

    return app
