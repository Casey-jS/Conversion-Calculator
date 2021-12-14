import unittest
from Controller import Controller as c

class TestUnit(unittest.TestCase):
    def test_binary(self):
        #Tests for Normal Input
        self.assertEqual(c.convert_num("Binary", "10101", "Decimal"), "21")
        self.assertEqual(c.convert_num("Binary", "10101", "Hex"), "15")
        self.assertEqual(c.convert_num("Binary", "10101", "Octal"), "25")
        self.assertEqual(c.convert_num("Binary", "10101", "Binary"), "10101")

    def test_binary_invalid(self):
        #Tests For Invalid Input
        self.assertEqual(c.convert_num("Binary", "hello", "Decimal"), "Invalid Entry")
        self.assertEqual(c.convert_num("Binary", "hello", "Hex"), "Invalid Entry")
        self.assertEqual(c.convert_num("Binary", "hello", "Octal"), "Invalid Entry")
        self.assertEqual(c.convert_num("Binary", "hello", "Binary"), "Invalid Entry")

        #Tests is Invalid input for Binary, but not for other inputs
        self.assertEqual(c.convert_num("Binary", "23", "Decimal"), "Invalid Entry")
        self.assertEqual(c.convert_num("Binary", "A", "Hex"), "Invalid Entry")
        self.assertEqual(c.convert_num("Binary", "29", "Octal"), "Invalid Entry")
        self.assertEqual(c.convert_num("Binary", "23", "Binary"), "Invalid Entry")
    
    def test_hex(self):
        #Tests for Normal Input
        self.assertEqual(c.convert_num("Hex", "2f", "Decimal"), "47")
        self.assertEqual(c.convert_num("Hex", "2f", "Hex"), "2f")
        self.assertEqual(c.convert_num("Hex", "2f", "Octal"), "57")
        self.assertEqual(c.convert_num("Hex", "2f", "Binary"), "101111")

    def test_hex_invalid(self):
        #Tests For Invalid Input
        self.assertEqual(c.convert_num("Hex", "hello", "Decimal"), "Invalid Entry")
        self.assertEqual(c.convert_num("Hex", "hello", "Hex"), "Invalid Entry")
        self.assertEqual(c.convert_num("Hex", "hello", "Octal"), "Invalid Entry")
        self.assertEqual(c.convert_num("Hex", "hello", "Binary"), "Invalid Entry")

    def test_decimal(self):
        #Tests for Normal Input
        self.assertEqual(c.convert_num("Decimal", "125", "Decimal"), "125")
        self.assertEqual(c.convert_num("Decimal", "125", "Hex"), "7d")
        self.assertEqual(c.convert_num("Decimal", "125", "Octal"), "175")
        self.assertEqual(c.convert_num("Decimal", "125", "Binary"), "1111101")

    def test_decimal_invalid(self):
        #Tests For Invalid Input
        self.assertEqual(c.convert_num("Decimal", "hello", "Decimal"), "Invalid Entry")
        self.assertEqual(c.convert_num("Decimal", "hello", "Hex"), "Invalid Entry")
        self.assertEqual(c.convert_num("Decimal", "hello", "Octal"), "Invalid Entry")
        self.assertEqual(c.convert_num("Decimal", "hello", "Binary"), "Invalid Entry")

        #Tests is Invalid input for Decimal, but not for other inputs
        self.assertEqual(c.convert_num("Decimal", "5a", "Hex"), "Invalid Entry")
   
    def test_octal(self):
        #Tests for Normal Input
        self.assertEqual(c.convert_num("Octal", "106", "Decimal"), "70")
        self.assertEqual(c.convert_num("Octal", "106", "Hex"), "46")
        self.assertEqual(c.convert_num("Octal", "106", "Octal"), "106")
        self.assertEqual(c.convert_num("Octal", "106", "Binary"), "1000110")

    def test_octal_invalid(self):
        #Tests For Invalid Input
        self.assertEqual(c.convert_num("Octal", "hello", "Decimal"), "Invalid Entry")
        self.assertEqual(c.convert_num("Octal", "hello", "Hex"), "Invalid Entry")
        self.assertEqual(c.convert_num("Octal", "hello", "Octal"), "Invalid Entry")
        self.assertEqual(c.convert_num("Octal", "hello", "Binary"), "Invalid Entry")
    
        #Tests is Invalid input for Octal, but not for other inputs
        self.assertEqual(c.convert_num("Octal", "2f", "Hex"), "Invalid Entry")


class TestNum(unittest.TestCase):
    def test_inch(self):
        #Tests Inch conversions
        self.assertEquals(round(c.convert_length("Inch", "100","Feet"),4), 8.3333)
        self.assertEquals(round(c.convert_length("Inch", "100","Yards"),4), 2.7778)
        self.assertEquals(round(c.convert_length("Inch", "100","Miles"),4), .0016)
        self.assertEquals(round(c.convert_length("Inch", "100","Centimeter"),4), 254.0)
        self.assertEquals(round(c.convert_length("Inch", "100","Meter"),4), 2.54)
        self.assertEquals(round(c.convert_length("Inch", "100","Kilometer"),4), .0025)
        self.assertEquals(round(c.convert_length("Inch", "100","Inch"),4), 100.0)

    def test_feet(self):
        #Tests Feet conversions
        self.assertEquals(round(c.convert_length("Feet", "10","Feet"),4), 10.0)
        self.assertEquals(round(c.convert_length("Feet", "10","Yards"),4), 3.3333)
        self.assertEquals(round(c.convert_length("Feet", "10","Miles"),4), .0019)
        self.assertEquals(round(c.convert_length("Feet", "10","Centimeter"),4), 304.8)
        self.assertEquals(round(c.convert_length("Feet", "10","Meter"),4), 3.0479)
        self.assertEquals(round(c.convert_length("Feet", "10","Kilometer"),4), .003)
        self.assertEquals(round(c.convert_length("Feet", "10","Inch"),4), 120.0)

    def test_yard(self):
        #Tests Yards conversions
        self.assertEquals(round(c.convert_length("Yards", "10","Feet"),4), 30.0)
        self.assertEquals(round(c.convert_length("Yards", "10","Yards"),4), 10.0)
        self.assertEquals(round(c.convert_length("Yards", "10","Miles"),4), .0057)
        self.assertEquals(round(c.convert_length("Yards", "10","Centimeter"),4), 914.4)
        self.assertEquals(round(c.convert_length("Yards", "10","Meter"),4), 9.144)
        self.assertEquals(round(c.convert_length("Yards", "10","Kilometer"),4), .0091)
        self.assertEquals(round(c.convert_length("Yards", "10","Inch"),4), 360.0)

    def test_miles(self):
        #Tests Mile conversions
        self.assertEquals(round(c.convert_length("Miles", "1","Feet"),4), 5280.0)
        self.assertEquals(round(c.convert_length("Miles", "1","Yards"),4), 1760.0)
        self.assertEquals(round(c.convert_length("Miles", "1","Miles"),4), 1.0)
        self.assertEquals(round(c.convert_length("Miles", "1","Centimeter"),4), 160934.0)
        self.assertEquals(round(c.convert_length("Miles", "1","Meter"),4), 1609.34)
        self.assertEquals(round(c.convert_length("Miles", "1","Kilometer"),4), 1.6093)
        self.assertEquals(round(c.convert_length("Miles", "1","Inch"),4), 63360.0)
    
    def test_centimeter(self):
        #Tests Centimeter conversions
        self.assertEquals(round(c.convert_length("Centimeter", "250","Feet"),4), 8.2021)
        self.assertEquals(round(c.convert_length("Centimeter", "250","Yards"),4), 2.734)
        self.assertEquals(round(c.convert_length("Centimeter", "250","Miles"),4), .0015)
        self.assertEquals(round(c.convert_length("Centimeter", "250","Centimeter"),4), 250.0)
        self.assertEquals(round(c.convert_length("Centimeter", "250","Meter"),4), 2.5)
        self.assertEquals(round(c.convert_length("Centimeter", "250","Kilometer"),4), .0025)
        self.assertEquals(round(c.convert_length("Centimeter", "250","Inch"),4), 98.4252)

    def test_meter(self):
        #Tests Centimer conversions
        self.assertEquals(round(c.convert_length("Meter", "3","Feet"),4), 9.843)
        self.assertEquals(round(c.convert_length("Meter", "3","Yards"),4), 3.282)
        self.assertEquals(round(c.convert_length("Meter", "3","Miles"),4), .0019)
        self.assertEquals(round(c.convert_length("Meter", "3","Centimeter"),4), 300.0)
        self.assertEquals(round(c.convert_length("Meter", "3","Meter"),4), 3.0)
        self.assertEquals(round(c.convert_length("Meter", "3","Kilometer"),4), .003)
        self.assertEquals(round(c.convert_length("Meter", "3","Inch"),4), 118.11)

    def test_kilometer(self):
        #Tests Centimer conversions
        self.assertEquals(round(c.convert_length("Kilometer", ".8","Feet"),4), 2624.8)
        self.assertEquals(round(c.convert_length("Kilometer", ".8","Yards"),4), 874.88)
        self.assertEquals(round(c.convert_length("Kilometer", ".8","Miles"),4), 0.4972)
        self.assertEquals(round(c.convert_length("Kilometer", ".8","Centimeter"),4), 80000.0)
        self.assertEquals(round(c.convert_length("Kilometer", ".8","Meter"),4), 800.0)
        self.assertEquals(round(c.convert_length("Kilometer", ".8","Kilometer"),4), .8)
        self.assertEquals(round(c.convert_length("Kilometer", ".8","Inch"),4), 31496.0)