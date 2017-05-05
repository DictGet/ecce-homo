import os.path

from flask import Flask, abort, request, send_from_directory, jsonify
from webargs.flaskparser import use_kwargs
from resizeimage.resizeimage import ImageSizeError

from .fields import image_args, correct_arguments
from .settings import MEDIA_ROOT, MEDIA_URL
from .utils import create_image, get_new_filename

app = Flask(__name__)


@app.route(os.path.join('/', MEDIA_URL, "<path:filename>"))
@use_kwargs(image_args, validate=correct_arguments)
def get_image(filename, **kwargs):
    """Endpoint for getting image.

    URL is e.g. /MEDIA_URL/path/to/image.jpg
    for an image at MEDIA_ROOT/path/to/image.jpg
    plus query params e.g. ?w=100&h=100&t=cover
    If base image exists, check if params image exists and if not create
    the image and return it.
    """

    # Check if base image exists
    absolute_path = os.path.join(MEDIA_ROOT, filename)
    if not os.path.isfile(absolute_path):
        abort(404)

    # Get new filename based on request url
    resized_filename = get_new_filename(filename, request)
    resized_absolute_path = os.path.join(MEDIA_ROOT, resized_filename)

    # Check if image exists already
    if os.path.isfile(resized_absolute_path):
        return send_from_directory(MEDIA_ROOT, resized_filename)

    # Create and return new image
    try:
        create_image(absolute_path, resized_absolute_path, **kwargs)
        if os.path.isfile(resized_absolute_path):
            return send_from_directory(MEDIA_ROOT, resized_filename)
    except IOError as e:
        abort(400, "An error occured trying to open the file.")
    except ImageSizeError as e:
        abort(400, e.message)


@app.errorhandler(400)
def custom_400_handler(error):
    """Handle bad requests adding a message to the response."""
    return jsonify({
        'messages': getattr(error, 'description', 'Invalid Request'),
    }), 400


@app.errorhandler(422)
def custom_422_handler(error):
    """Handle unprocessable_entity requests adding an error to the response.

    Errors as thrown by  webargs library for invalid parameters.
    """
    exception = getattr(error, 'exc')
    return jsonify({
        'messages': exception.messages if exception else "Invalid Request"
    }), 422


if __name__ == "__main__":
    app.run()
