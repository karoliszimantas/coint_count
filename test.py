'''Main application testing'''

import unittest
import script

class TestCoinCount(unittest.TestCase):
    def test_coincount(self):
        self.assertEqual(script.coin_count(45),{20: 2, 4: 1, 1: 1})

    def test_coincount_1(self):
        self.assertEqual(script.coin_count(25),{20: 1, 4: 1, 1:1})

    def test_coincount_2(self):
        self.assertEqual(script.coin_count(55),{20: 2, 15:1})

    def test_coincount_3(self):
        self.assertEqual(script.coin_count(37),{20: 1, 15:1, 1:2})

    def test_coincount_4(self):
        self.assertEqual(script.coin_count(17),{15:1, 1:2})

    def test_coincount_5(self):
        self.assertEqual(script.coin_count(4),{4:1})

    def test_coincount_6(self):
        self.assertEqual(script.coin_count(19),{15:1, 4:1})

    def test_coincount_7(self):
        self.assertEqual(script.coin_count(22),{20: 1, 1:2})

    def test_coincount_error(self):
        self.assertNotEqual(script.coin_count(43),{20: 1, 15: 1, 4:1, 1:4})

if __name__ == '__main__':
    unittest.main()
