from flask import Flask

webui = Flask(__name__)
from webui import views  # noqa: E402,F401
