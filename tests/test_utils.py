import unittest
from utils import get_number_from_filename, get_ordered_scripts

# run tests:
# $ python run_tests.py test_db.py tests

class test_utils(unittest.TestCase):

    def test_get_number_from_filename(self):
        self.assertEqual(45, get_number_from_filename('045.createtable.sql'))
        self.assertEqual(45, get_number_from_filename('045createtable.sql'))
        self.assertEqual(45, get_number_from_filename('045.crea5678tetable.sql'))
        self.assertEqual(None, get_number_from_filename('foobar045.createtable.sql'))


