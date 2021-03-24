import unittest
import math


class MathCeilTest(unittest.TestCase):
    def test_regular_case(self):
        self.assertEqual(math.ceil(6.11), 7)

    def test_far_value(self):
        self.assertEqual(math.ceil(0.000000000000000000000000000000001), 1)

    def test_close_value(self):
        self.assertEqual(math.ceil(1.999999999999999999999999999999999), 2)

    def test_negative_value(self):
        self.assertEqual(math.ceil(-1.025), -1)

    def test_operation(self):
        self.assertEqual(math.ceil(3.1 * 5), 16)

    def test_wrong_result(self):
        self.assertNotEqual(math.ceil(2.40), 2)

    def test_chained_operation(self):
        self.assertEqual(math.ceil(9.8) + 5, 15)

    def test_several_calls(self):
        for i in range(100):
            self.assertEqual(math.ceil(i + 0.3), i+1)

    def test_string_argument(self):
        self.assertRaises(TypeError, math.ceil, "23.34")

    def test_none_argument(self):
        self.assertRaises(TypeError, math.ceil, None)

    def test_integer_argument(self):
        self.assertEqual(math.ceil(88), 88)


if __name__ == '__main__':
    unittest.main()
