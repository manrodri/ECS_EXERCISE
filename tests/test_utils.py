import unittest
import utils

# run tests:
# $ python run_tests.py test_db.py tests

class test_utils(unittest.TestCase):

    def test_get_number_from_filename(self):
        self.assertEqual(45, utils.get_number_from_filename('045.createtable.sql'))
        self.assertEqual(45, utils.get_number_from_filename('045createtable.sql'))
        self.assertEqual(45, utils.get_number_from_filename('045.crea5678tetable.sql'))
        self.assertEqual(None, utils.get_number_from_filename('foobar045.createtable.sql'))
    
    def test_get_scripts(self):
        path = '/home/ubuntu/ECS_user_case/SQL_scripts'
        scripts = utils.get_scripts(path)
        self.assertEqual(5, len(scripts))
        self.assertIn('015.createTable.sql', scripts)
    
    def test_ordered_scripts(self):
        scripts = ['234.foo.sql', '12bar.sql', '1111.knight.sql']
        result = utils.get_ordered_scripts(scripts)
        
        self.assertTrue(type(result) is tuple)
        self.assertEqual(['1111.knight.sql', '12bar.sql', '234.foo.sql'], result[0])
        self.assertDictEqual(result[1], {'1111.knight.sql': 1111, '234.foo.sql': 234, '12bar.sql': 12})
        
    
         

