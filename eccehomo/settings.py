import os

MEDIA_DIRECTORY_ROOT = '/home/mikethomas/ecce-homo/media/'

DEFAULT_METHOD = os.environ.get('ECCEHOMO_DEFAULT_METHOD', 'contain')

RESIZE_METHODS = ['contain', 'crop', 'cover', 'thumbnail']

MINIMUM_LENGTH = os.environ.get('ECCEHOMO_MINIMUM_LEGNTH', 10)
