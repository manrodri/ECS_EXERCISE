import os
import sys

import unittest
import logging

scriptdir = os.getcwd()
libdir = os.path.join(scriptdir, 'lib')
sys.path.insert(0, libdir)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('[%(levelname)-2s] %(message)s')
handler.setFormatter(formatter)


if __name__ == '__main__':


    pattern = sys.argv[1] if len(sys.argv) >=2 else "test*.py"
    if pattern == 'all':
        pattern = "test*.py"
    test_dir = sys.argv[2] if len(sys.argv) >=3 else "tests"

    sys.path.insert(0, test_dir)
    print("Running {} within {}".format(pattern, test_dir))

    test_loader = unittest.defaultTestLoader.discover(test_dir, pattern)
    test_runner = unittest.TextTestRunner()
    result = test_runner.run(test_loader)

    sys.exit(not result.wasSuccessful())
