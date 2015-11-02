import unittest

from ..algorithms.selection_sort import SelectionSort


class SelectionSortTests(unittest.TestCase):

    def setUp(self):
        self.obj = SelectionSort([0, 2, 3, 4, 5, 7, 8, 9, 10, 1])

    def test_swap(self):
        self.obj.swap(0, 1)
        self.assertEqual(self.obj.list, [2, 0, 3, 4, 5, 7, 8, 9, 10, 1])

    def test_find_min(self):
        min_index = self.obj.findMin(1)
        self.assertEqual(min_index, 9)


    def test_sorted(self):
        new_list = self.obj.sort()
        self.assertEqual(new_list, [0, 1, 2, 3, 4, 5, 7 ,8 ,9, 10])
