import unittest
import Model
from Controller import *

class TestConversions(unittest.TestCase):

    def test_bin_check(self): self.assertTrue(Model.is_binary('101010'))
    def test_bin_check2(self): self.assertFalse(Model.is_binary('11010102'))

    def test_hex_check(self): self.assertTrue(Model.is_hex('fd449'))
    def test_hex_check2(self): self.assertFalse(Model.is_hex('36273g'))
    
    def test_dec_check(self): self.assertTrue(Model.is_decimal('1129'))
    def test_dec_check2(self): self.assertFalse(Model.is_decimal('11a'))

    def test_oct_check(self): self.assertTrue(Model.is_octal('11765'))
    def test_oct_check2(self): self.assertFalse(Model.is_octal('11458'))

    def test_bin2dec(self): self.assertEqual(Model.bin_to_dec('10000'), '16')
    def test_bin2hex(self): self.assertEqual(Model.bin_to_hex('10000'), '10')
    def test_bin2oct(self): self.assertEqual(Model.bin_to_oct('10000'), '20')

    def test_dec2bin(self): self.assertEqual(Model.dec_to_bin('13'), '1101')
    def test_dec2hex(self): self.assertEqual(Model.dec_to_hex('13'), 'd')
    def test_dec2oct(self): self.assertEqual(Model.dec_to_oct('13'), '15')

    def test_hex2dec(self): self.assertEqual(Model.hex_to_dec('d'), '13')
    def test_hex2bin(self): self.assertEqual(Model.hex_to_bin('d'), '1101')
    def test_hex2oct(self): self.assertEqual(Model.hex_to_oct('d'), '15')

    def test_oct2dec(self): self.assertEqual(Model.oct_to_dec('15'), '13')
    def test_oct2bin(self): self.assertEqual(Model.oct_to_bin('15'), '1101')
    def test_oct2hex(self): self.assertEqual(Model.oct_to_hex('15'), 'd')


    
    

    


if __name__ == '__main__':
    unittest.main()