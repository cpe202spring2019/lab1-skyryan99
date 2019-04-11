import unittest
from location import *

class TestLab1(unittest.TestCase):

   def test_repr(self):
      loc = Location("SLO", 35.3, -120.7)
      self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
   def test_eq(self):
      loc1 = Location("Santa Cruz", 22.2, 22.2)
      loc2 = Location("Santa Cruz", 22.2, 22.2)
      self.assertTrue(loc1 == loc2)

if __name__ == "__main__":
   unittest.main()
