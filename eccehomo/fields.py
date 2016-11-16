from webargs import fields
from .settings import RESIZE_METHODS

image_args = {
    'w': fields.Int(validate=lambda val: val > 1),
    'h': fields.Int(validate=lambda val: val > 1),
    't': fields.Str(validate=lambda val: val in RESIZE_METHODS)
}
