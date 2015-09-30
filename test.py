from webui import webui
from flask_zurb_foundation import Foundation

import os
import unittest
import tempfile

Foundation(webui)

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
      webui.config['TESTING'] = True
      self.app = webui.test_client(self)

    def tearDown(self):
      pass

    def test_response_code(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 200)

    def test_response(self):
        rv = self.app.get('/')
        self.assertTrue("logo.png" in rv.data)

    def test_404_response(self):
        rv = self.app.get('/testurl')
        self.assertTrue("logo.png" in rv.data)


if __name__ == '__main__':
    unittest.main()
