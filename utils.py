from PIL import Image
from resizeimage import resizeimage
from settings import DEFAULT_METHOD


def create_image(filename, new_filename, **kwargs):
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
    return resize_image(filename, new_filename, method, size)


def resize_image(filename, new_filename, method, size):
    try:
        with open(filename, 'r+b') as f:
            with Image.open(f) as image:
                resized = resizeimage.resize(method, image, size)
                resized.save(new_filename, image.format)
    except Exception as e:
        print e
        return False
    return True


def get_new_filename(request):
    """There's no built-in to give path and parameters all together so
    do it manually."""

    # Remove url root
    path = request.url.split(request.url_root)[1]
    if '/?' not in path:
        return path

    # Remove trailing '/' between path and parameters
    split_path = path.split('/?')
    clean_path = split_path[0] + '?' + split_path[1]
    return clean_path
