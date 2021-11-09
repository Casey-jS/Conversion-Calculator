import unittest
import Model
from Controller import Controller

class TestConversions(unittest.TestCase):

    def test_dec_bin(self):
        self.assertEqual(10000, Model.dec_to_bin(16), "Nope")
    
    def test_button(self):
        correct = convert_num("Binary", 16, "Decimal")
        self.assertEqual(correct, 10000)

if __name__ == '__main__':
    unittest.main()