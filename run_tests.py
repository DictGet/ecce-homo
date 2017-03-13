import tempfile
import os
import re

import nose


def run_tests():
    root = tempfile.mkdtemp()
    os.environ['ECCEHOMO_MEDIA_ROOT'] = root
    print root
    os.environ['ECCEHOMO_MEDIA_URL'] = 'media'
    os.environ['ECCEHOMO_DEFAULT_METHOD'] = 'contain'
    os.environ['ECCEHOMO_MINIMUM_LEGNTH'] = '10'

    noseconfig = nose.config.Config()
    noseconfig.verbosity = 3
    noseconfig.ignoreFiles.append(re.compile(r'^run_tests.py'))
    nose.run(config=noseconfig)


if __name__ == '__main__':
    run_tests()
