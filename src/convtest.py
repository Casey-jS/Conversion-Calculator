import unittest
import Model

class TestConversions(unittest.TestCase):

    def test_dec_bin(self):
        self.assertEqual(10000, Model.dec_to_bin(16), "Nope")
    
    def test_dec_hex(self):
        self.assertEqual()

if __name__ == '__main__':
    unittest.main()