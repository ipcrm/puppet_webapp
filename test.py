from webui import webui

import os
import unittest
import tempfile

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

    def test_response_tagline(self):
        rv = self.app.get('/')
        self.assertTrue("The shortest path to better" in rv.data)
        self.assertTrue("software" in rv.data)

    def test_response_tagline_dynamic(self):
        rv = self.app.get('/automation')
        self.assertTrue("The shortest path to better" in rv.data)
        self.assertTrue("automation" in rv.data)


    def test_404_response(self):
        rv = self.app.get('/testurl')
        self.assertTrue("logo.png" in rv.data)

if __name__ == '__main__':
    unittest.main()
