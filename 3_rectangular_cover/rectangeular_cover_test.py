
import unittest
from rectangeular_cover import solution

class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution(0), 0)
        self.assertEqual(solution(1), 1)
        self.assertEqual(solution(2), 2)
        self.assertEqual(solution(3), 3)
        self.assertEqual(solution(4), 5)
        self.assertEqual(solution(5), 8)

if __name__ == '__main__':
    unittest.main()
