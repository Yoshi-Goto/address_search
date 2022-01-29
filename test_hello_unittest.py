import unittest


def ka(x, y):
    return x + y


def gen(x, y):
    return x - y


def jyou(x, y):
    return x * y


def jyo(x, y):
    return x / y


class MyTestCase(unittest.TestCase):
    def test_tasu(self):
        self.assertEqual(7, ka(3, 4))  # add assertion here

    def test_hiku(self):
        self.assertEqual(1, gen(4, 3))  # add assertion here

    def test_kakeru(self):
        self.assertEqual(9, jyou(4, 3))  # add assertion here

    def test_waru(self):
        self.assertEqual(2, jyo(6, 2))  # add assertion here


if __name__ == '__main__':
    unittest.main()
