import unittest
import phonebook_app as pb


class TestPB(unittest.TestCase):

    def test_valid_number(self):
        test_cases = {
            "10-100-20-30": True,
            "101002030": False,
            "10-203040": False,
            "2030-2030-30": False
        }

        for num, result in test_cases.items():
            with self.subTest():
                self.assertEqual(pb.valid_phone_number(num), result)

unittest.main()