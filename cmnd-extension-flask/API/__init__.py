from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS

# Load environment variables
load_dotenv()


def create_app():
    app = Flask(__name__)
    CORS(app)

    from .endpoints import cmnd_tools

    app.register_blueprint(cmnd_tools, url_prefix='/')

    return app