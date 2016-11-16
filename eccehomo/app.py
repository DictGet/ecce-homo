import os

from flask import Flask, abort, request, send_from_directory
from webargs.flaskparser import use_kwargs

from .fields import image_args
from .settings import MEDIA_DIRECTORY_ROOT
from .utils import create_image, get_new_filename

app = Flask(__name__)


@app.route("/<path:filename>", strict_slashes=False)
@use_kwargs(image_args)
def get_image(filename, **kwargs):
    filename = MEDIA_DIRECTORY_ROOT + filename
    if not os.path.isfile(filename):
        abort(404)
    new_filename = get_new_filename(request)
    if os.path.isfile(new_filename):
        return send_from_directory(MEDIA_DIRECTORY_ROOT, new_filename)
    if create_image(filename, new_filename, **kwargs):
        return send_from_directory(MEDIA_DIRECTORY_ROOT, new_filename)
    abort(500)


if __name__ == "__main__":
    app.run()
