
import unittest

from climb_n_stair_case import climb_n

class TestSolution(unittest.TestCase):
    
    def test_climb_n(self):
        self.assertEqual(climb_n(1), 1)
        self.assertEqual(climb_n(2), 2)
        self.assertEqual(climb_n(3), 4)
        
        
if __name__ == '__main__':
    unittest.main()