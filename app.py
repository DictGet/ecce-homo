import os

from flask import Flask, abort, send_file

app = Flask(__name__)


@app.route("/<path:filename>/")
def get_image(filename):
    if not os.path.isfile(filename):
        abort(404)
    return send_file(filename)


if __name__ == "__main__":
    app.run()
