import unittest

from serach_address import search_address


class MyTestCase(unittest.TestCase):
    def test_something1(self):
        zipcode = "0287302"
        actual = search_address(zipcode)
        expected = [
            "岩手県八幡平市八幡平温泉郷",
            "岩手県八幡平市松尾寄木",
            "岩手県八幡平市松川温泉"
        ]
        self.assertEqual(expected, actual)  # add assertion here

    def test_something2(self):
        actual = search_address("00")
        expected = "郵便番号はハイフンなし7桁で入力してください。"
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
