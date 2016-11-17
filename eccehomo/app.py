import os

from flask import Flask, abort, request, send_from_directory, jsonify
from webargs.flaskparser import use_kwargs

from .fields import image_args, correct_arguments
from .settings import MEDIA_DIRECTORY_ROOT
from .utils import create_image, get_new_filename

app = Flask(__name__)


@app.route("/<path:filename>", strict_slashes=False)
@use_kwargs(image_args, validate=correct_arguments)
def get_image(filename, **kwargs):
    absolute_path = MEDIA_DIRECTORY_ROOT + filename
    if not os.path.isfile(absolute_path):
        abort(404)

    resized_filename = get_new_filename(request)
    resized_absolute_path = MEDIA_DIRECTORY_ROOT + resized_filename

    if os.path.isfile(resized_absolute_path):
        return send_from_directory(MEDIA_DIRECTORY_ROOT, resized_filename)

    if create_image(absolute_path, resized_absolute_path, **kwargs):
        return send_from_directory(MEDIA_DIRECTORY_ROOT, resized_filename)
    abort(500)


@app.errorhandler(422)
def handle_unprocessable_entity(err):
    exception = getattr(err, 'exc')
    if exception:
        messages = err.exc.messages
    else:
        messages = ['Invalid request']
    return jsonify({
        'messages': messages,
    }), 422


if __name__ == "__main__":
    app.run()
