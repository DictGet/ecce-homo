import unittest

from webargs import missing

from .. import utils


class TestResizeArguments(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.filename = "filename"
        self.new_filename = "new_filename"

    def test_default_method_assigned(self):
        w = 100
        h = 50
        t = missing
        kwargs = {'w': w, 'h': h, 't': t}
        filename, new_filename, method, size = utils.get_resize_arguments(
            self.filename, self.new_filename, **kwargs)
        self.assertEqual(method, 'contain')
        self.assertEqual(size, [w, h])

    def test_width_method_when_t_empty(self):
        w = 100
        h = missing
        t = missing
        kwargs = {'w': w, 'h': h, 't': t}
        filename, new_filename, method, size = utils.get_resize_arguments(
            self.filename, self.new_filename, **kwargs)
        self.assertEqual(method, 'width')
        self.assertEqual(size, w)

    def test_height_method_when_t_empty(self):
        filename = "filename"
        new_filename = "new_filename"
        w = missing
        h = 100
        t = missing
        kwargs = {'w': w, 'h': h, 't': t}
        filename, new_filename, method, size = utils.get_resize_arguments(
            filename, new_filename, **kwargs)
        self.assertEqual(method, 'height')
        self.assertEqual(size, h)
