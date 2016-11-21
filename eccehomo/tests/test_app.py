import unittest

from eccehomo.app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True
        self.app.debug = True

    def test_width_image(self):
        result = self.app.get('/media/test_image.jpg?w=100')
        self.assertEqual(result.status_code, 200)

    def test_height_image(self):
        result = self.app.get('/media/test_image.jpg?h=100')
        self.assertEqual(result.status_code, 200)

    def test_default_image(self):
        result = self.app.get('/media/test_image.jpg?w=100&h=100')
        self.assertEqual(result.status_code, 200)

    def test_crop_image(self):
        result = self.app.get('/media/test_image.jpg?w=100&h=100&t=crop')
        self.assertEqual(result.status_code, 200)

    def test_explicit_default_fails(self):
        result = self.app.get('/media/test_image.jpg?w=100&h=100&t=contain')
        self.assertEqual(result.status_code, 422)
