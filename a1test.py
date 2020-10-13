# Name : Manasvi Singh
# Roll No : 2019369
# Group : 1

import unittest
from a1 import changeBase

# TEST cases should cover the different boundary cases.

class testpoint(unittest.TestCase):
    
    def test_change_base(self):
        self.assertEqual(changeBase(1, "INR", "GBP", "2010-10-25"), 0.014340456298200513)
        
        self.assertEqual(changeBase(1, "INR", "CAD","2017-10-09"),0.019190359876241656 )
        self.assertEqual(changeBase(100,"EUR","EUR","2017-10-09"),100.0)
        self.assertAlmostEqual(changeBase(100, "CAD", "GBP", "2010-10-25"),62.4553915051)
        self.assertAlmostEqual(changeBase(100, "EUR", "INR", "2010-10-25"),6224.0)
        self.assertAlmostEqual(changeBase(1, "INR", "GBP", "2010-10-25"),0.014340456298200513,delta=0.1)





if __name__=='__main__':
    unittest.main()




