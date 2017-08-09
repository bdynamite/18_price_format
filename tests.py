import unittest

from format_price import format_price


class TestCase(unittest.TestCase):

    def test_1(self):
        self.assertRaises(ValueError, format_price, 'fwf223')
        
    def test_2(self):
        self.assertRaises(ValueError, format_price, range(5))

    def test_3(self):
        self.assertRaises(ValueError, format_price, -453.54)

    def test_4(self):
        self.assertRaises(ValueError, format_price, -0.0000242)

    def test_5(self):
        self.assertRaises(ValueError, format_price, 0.00005242)

    def test_6(self):
        price = format_price(0.009673672)
        self.assertEqual(price, '0.01')

    def test_7(self):
        price = format_price(765)
        self.assertEqual(price, '765.00')

    def test_8(self):
        price = format_price('875690')
        self.assertEqual(price, '875 690.00')

    def test_9(self):
        price = format_price(7568.9875)
        self.assertEqual(price, '7 568.99')

    def test_10(self):
        price = format_price('7544.8512')
        self.assertEqual(price, '7 544.85')

if __name__ == '__main__':
    unittest.main()