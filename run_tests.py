import os
import nose
from PIL import Image
from eccehomo import test_settings

# Create Test media Folder
if not os.path.isdir(test_settings.TEST_MEDIA_ROOT):
    os.mkdir(test_settings.TEST_MEDIA_ROOT)

test_settings.filename = os.path.join(test_settings.TEST_MEDIA_ROOT,
                                      'test_image.jpg')
if not os.path.isfile(test_settings.filename):
    image = Image.new('RGBA', size=(500, 500), color=(155, 0, 0))
    image.save(test_settings.filename, 'jpeg')

# Set environment variables for tests
os.environ['ECCEHOMO_MEDIA_ROOT'] = test_settings.TEST_MEDIA_ROOT
os.environ['ECCEHOMO_MEDIA_URL'] = 'media'
os.environ['ECCEHOMO_DEFAULT_METHOD'] = 'contain'
os.environ['ECCEHOMO_MINIMUM_LEGNTH'] = '10'


noseconfig = nose.config.Config()
nose.run(config=noseconfig)
