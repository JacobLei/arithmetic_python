
import unittest
from yang_matrix import find

class TestSolution(unittest.TestCase):

    def test_find(self):
        l = [[1, 3, 5],
             [2, 7, 9],
             [4, 8, 19]
            ]
        self.assertEqual(find(l, 1), True)
        self.assertEqual(find(l, 6), False)
    
if __name__ == '__main__':
    unittest.main()

