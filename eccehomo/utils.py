import six

if six.PY2:
    from urlparse import urlparse
else:
    from urllib.parse import urlparse

from PIL import Image

from resizeimage import resizeimage

from .settings import DEFAULT_METHOD


def get_resize_arguments(**kwargs):
    width = kwargs.get('w')
    height = kwargs.get('h')
    method = kwargs.get('t')

    if not method:
        if width:
            method = DEFAULT_METHOD if height else 'width'
            size = [width, height] if height else width
        elif height:
            method = 'height'
            size = height
    else:
        size = [width, height]
    return method, size


def create_image(filename, new_filename, **kwargs):
    method, size = get_resize_arguments(**kwargs)
    resize_image(filename, new_filename, method, size)


def resize_image(filename, new_filename, method, size):
    """Resize an image according to a method and size and store it

    :param filename: file to resize
    :param new_filename: Name of the resized file
    :param method: resize method to use
    :param size:

    :raise IOError: Bad file or filename
    :raise ImageSizeError: Wrong image size
    """
    with open(filename, 'r+b') as f:
        with Image.open(f) as image:
            resized = resizeimage.resize(method, image, size)
            resized.save(new_filename, image.format)


def get_new_filename(filename, request):
    """There's no built-in to give path and parameters all together so
    do it manually."""
    return "{}?{}".format(filename, urlparse(request.url).query)
