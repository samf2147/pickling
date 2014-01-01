from pickler import list_pickler, unpickler
import os
import unittest

class PickleTest(unittest.TestCase):
    def setUp(self):
        self.list = ['a','b','c','d']
        list_pickler(self.list,'test_list.pkl')
    
    def test_pickled_equality(self):
        self.recovered_list = unpickler('test_list.pkl')
        self.assertEqual(self.list, self.recovered_list)
    
    def tearDown(self):
        os.remove('test_list.pkl')