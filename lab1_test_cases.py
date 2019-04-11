import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter2(self):
        self.assertEqual(max_list_iter([1, 2, 3, 4]), 4)
    
    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_reverse_rec2(self):
        self.assertEqual(reverse_rec([1, 2, 4, -2, -4, 3]), [3, -4, -2, 4, 2, 1])

    def test_reverse_rec3(self):
        self.assertEqual(reverse_rec([4]), [4])

    def test_reverse_rec4(self):
        self.assertEqual(reverse_rec([]), [])

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

    def test_bin_search2(self):
       list_val = [0, 2, 4, 6, 8, 10, 12, 14, 16]
       low = 0
       high = len(list_val) - 1
       self.assertEqual(bin_search(8, 0, len(list_val) - 1, list_val), 4)

    def test_bin_search3(self):
       list_val = [0, 2, 3, 4, 5, 6, 7, 8, 9]
       low = 0
       high = len(list_val) - 1
       self.assertEqual(bin_search(1, 0, len(list_val) - 1, list_val), None)

if __name__ == "__main__":
        unittest.main()

    
