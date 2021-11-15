import unittest
import Model
from Controller import *

class TestConversions(unittest.TestCase):

    def test_dec_bin(self):
        self.assertEqual('10000', Model.dec_to_bin(16), "Nope")
    
    def test_bin_check(self):
        self.assertFalse(Model.is_binary('11010102'))
        
    def test_bin_check2(self):
        self.assertTrue(Model.is_binary('11010101'))


if __name__ == '__main__':
    unittest.main()