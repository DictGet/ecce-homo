from urlparse import urlparse

from PIL import Image
from resizeimage import resizeimage

from .settings import DEFAULT_METHOD


def create_image(filename, new_filename, **kwargs):
    return resize_image(get_resize_arguments(filename, new_filename, **kwargs))


def get_resize_arguments(filename, new_filename, **kwargs):
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


def resize_image(filename, new_filename, method, size):
    """
    Opens file 'filename'. Resized with 'method' to 'size'
    and saves as 'new_filename'.
    Bad file or filename raises IOError
    Wrong image size raises ImageSizeError
    """
    with open(filename, 'r+b') as f:
        with Image.open(f) as image:
            resized = resizeimage.resize(method, image, size)
            resized.save(new_filename, image.format)


def get_new_filename(filename, request):
    """There's no built-in to give path and parameters all together so
    do it manually."""
    query = urlparse(request.url).query
    return "{}?{}".format(filename, query)
