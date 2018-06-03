import unittest

from fib import f
from fib_class import Solution
from fib_lambda import fib
from memo_climb_stair import memo_fib
from fib_range import fib_range

class TestSolution(unittest.TestCase):

    def test_f(self):
        self.assertEqual(f(1), 1)
        self.assertEqual(f(2), 2)
        self.assertEqual(f(3), 3)
        self.assertEqual(f(4), 5)
        self.assertEqual(f(10), 89)
    
    def test_climb_stair(self):
        solution = Solution()
        self.assertEqual(solution.climb_stair(1), 1)
        self.assertEqual(solution.climb_stair(2), 2)
        self.assertEqual(solution.climb_stair(3), 3)
        self.assertEqual(solution.climb_stair(4), 5)
        self.assertEqual(solution.climb_stair(10), 89)
        
    def test_fib(self):
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 2)
        self.assertEqual(fib(3), 3)
        self.assertEqual(fib(4), 5)
        self.assertEqual(fib(10), 89)
        
    def test_memo_fib(self):
        self.assertEqual(memo_fib(1), 1)
        self.assertEqual(memo_fib(2), 2)
        self.assertEqual(memo_fib(3), 3)
        self.assertEqual(memo_fib(4), 5)
        self.assertEqual(memo_fib(10), 89)
        
    def test_fib_range(self):
        self.assertEqual(fib_range(1), 1)
        self.assertEqual(fib_range(2), 2)
        self.assertEqual(fib_range(3), 3)
        self.assertEqual(fib_range(4), 5)
        self.assertEqual(fib_range(10), 89)
       
if __name__ == '__main__':
    unittest.main()
        
        