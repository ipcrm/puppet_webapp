from flask import render_template
from webui import webui

@webui.route('/')
@webui.route('/index')

@webui.errorhandler(404)
def page_not_found(e):
    return render_template('index.html')
