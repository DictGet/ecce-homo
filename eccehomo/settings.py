import os
import os.path

MEDIA_ROOT = os.path.join('/', os.environ.get('ECCEHOMO_MEDIA_ROOT', ''))

MEDIA_URL = os.environ.get('ECCEHOMO_MEDIA_URL', '')

DEFAULT_METHOD = os.environ.get('ECCEHOMO_DEFAULT_METHOD', 'contain')

MINIMUM_LENGTH = int(os.environ.get('ECCEHOMO_MINIMUM_LEGNTH', 10))
