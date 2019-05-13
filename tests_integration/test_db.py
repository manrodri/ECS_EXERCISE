import unittest
import utils


# run tests:
# $ python run_tests.py test_db.py tests


class test_db(unittest.TestCase):
    
    def setUp(self):
        self.db_url = 'mysql://root:password@localhost/integration'
    
    
    def test_update_db_version(self):
        result =utils.update_db_version(self.db_url, 85)
        self.assertEqual(85, result)
    
    def test_get_db_version(self):
        session = utils.create_connection(self.db_url)
        version = utils.get_db_version(session)
        self.assertEqual(85, version)
    
        


