#!env/bin/python
from webui import webui
from flask_zurb_foundation import Foundation

Foundation(webui)

if __name__ == "__main__":
      webui.run()
