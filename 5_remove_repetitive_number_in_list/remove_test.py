
import unittest
from remove_by_set import remove_by_set
from remove_by_dict import remove_by_dict
from remove_by_list_comprehension import remove_by_list_comprehension

class TestSolution(unittest.TestCase):

    l = [ 1, 1, 2, 4, 3, 2, 3, 3]

    def test_remove_by_set(self):
        self.assertEqual(remove_by_set(self.l), [1, 2, 3, 4])

    def test_remove_by_dict(self):
        self.assertEqual(remove_by_dict(self.l), [1, 2, 3, 4])

    def test_remove_by_list_comprehension(self):
        self.assertEqual(remove_by_list_comprehension(self.l), [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
