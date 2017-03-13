from webargs import fields
from webargs.core import ValidationError

from . import settings


RESIZE_METHODS = ['contain', 'crop', 'cover', 'thumbnail']


def type_allowed(val):
    if val == settings.DEFAULT_METHOD:
        raise ValidationError(
            'Default type cannot be explicity chosen. Omit t parameter.',
            status_code=422)
    if val not in RESIZE_METHODS:
        raise ValidationError(
            'Resize type parameter not recognized',
            status_code=422)


def correct_arguments(args):
    if not args.get('w') and not args.get('h'):
        raise ValidationError(
            'Must provide at least one length parameter,w or h.',
            status_code=422)
    if args.get('t'):
        if not args.get('w') or not args.get('h'):
            raise ValidationError(
                'Must provide both w and h for this method.',
                status_code=422)


image_args = {
    'w': fields.Int(validate=lambda val: val > settings.MINIMUM_LENGTH),
    'h': fields.Int(validate=lambda val: val > settings.MINIMUM_LENGTH),
    't': fields.Str(validate=type_allowed)
}
