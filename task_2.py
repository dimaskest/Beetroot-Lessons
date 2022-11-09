import unittest
from task_1_manager import CManager as CM


class TestCM(unittest.TestCase):

    def test_num_of_usage(self):
        self.assertEqual(CM("poem.txt", "r").get_num_of_usage(), 0)
    
    def test_exc(self):
        self.assertIsInstance(CM("poem.txt", "r").uppercase(), AttributeError)

unittest.main()