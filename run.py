#!env/bin/python
from webui import webui
from flask_zurb_foundation import Foundation

Foundation(webui)
webui.run(debug=True)
