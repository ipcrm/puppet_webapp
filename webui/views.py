from flask import render_template
from webui import webui
import pkg_resources 
version = pkg_resources.require("webui")[0].version

@webui.route('/')
@webui.route('/index')
@webui.route('/<tagline>')
def index(tagline='software'):
    return render_template('index.html', tagline=tagline, version=version)

@webui.errorhandler(404)
def page_not_found(e):
    return render_template('index.html')
