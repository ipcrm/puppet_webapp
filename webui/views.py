from flask import render_template
from webui import webui

@webui.route('/')
@webui.route('/index')
def index():
    return render_template('index.html')
