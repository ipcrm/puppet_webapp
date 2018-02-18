from flask import render_template
from webui import webui
from ._version import __version__


@webui.route('/')
@webui.route('/index')
@webui.route('/<tagline>')
def index(tagline='software'):
    return render_template('index.html',
                           tagline=tagline,
                           version=__version__,
                           )


@webui.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', version=__version__), 404
