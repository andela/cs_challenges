import unittest

from ..algorithms.insertion_sort import InsertionSort


class InsertionSortTests(unittest.TestCase):

    def setUp(self):
        self.obj = InsertionSort([10, 2, 3, 4, 5, 7, 8, 9, 0, 1])

    def test_swap(self):
        self.obj.swap(0, 1)
        self.assertEqual(self.obj.list, [2, 10, 3, 4, 5, 7, 8, 9, 0, 1])

    def test_bubble_last(self):
        list = [0, 1, 2, -1, 1]
        obj = InsertionSort(list)
        obj.bubbleLast(3)
        self.assertEqual(obj.list, [-1, 0, 1, 2, 1])

    def test_sorted(self):
        new_list = self.obj.sort()
        self.assertEqual(new_list, [0, 1, 2, 3, 4, 5, 7 ,8 ,9, 10])
