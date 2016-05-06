from flask import render_template
from webui import webui

@webui.route('/')
@webui.route('/index')
@webui.route('/<tagline>')
def index(tagline='software'):
    return render_template('index.html', tagline=tagline)

@webui.errorhandler(404)
def page_not_found(e):
    return render_template('index.html')
