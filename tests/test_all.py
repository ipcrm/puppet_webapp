from webui import webui
import unittest


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
        self.assertTrue("logo.png" in str(rv.data))

    def test_response_tagline(self):
        rv = self.app.get('/')
        self.assertTrue("The shortest path to better" in str(rv.data))
        self.assertTrue("software" in str(rv.data))

    def test_response_tagline_dynamic(self):
        rv = self.app.get('/automation')
        self.assertTrue("The shortest path to better" in str(rv.data))
        self.assertTrue("automation" in str(rv.data))

    def test_404_response(self):
        rv = self.app.get('/testurl/testurl')
        self.assertEqual(rv.status_code, 404)
        self.assertTrue("Whoops!" in str(rv.data))


if __name__ == '__main__':
    unittest.main()
