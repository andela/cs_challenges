import unittest

from ..algorithms.quick_sort import QuickSort


class QuickSortTests(unittest.TestCase):

    def setUp(self):
        self.obj = QuickSort([10, 2, 3, 4, 5, 7, 8, 9, 0, 1])

    def test_swap(self):
        self.obj.swap(0, 1)
        self.assertEqual(self.obj.list, [2, 10, 3, 4, 5, 7, 8, 9, 0, 1])

    def test_partition(self):
        list = [12, 7, 14, 9, 10, 11]
        obj = QuickSort(list)
        pivot = obj.partition(0, 5)
        self.assertEqual(pivot, 3)
        self.assertEqual(obj.list[pivot], 11)
        self.assertEqual(obj.list, [7, 9, 10, 11, 14, 12])

    def test_sorted(self):
        new_list = self.obj.sort()
        self.assertEqual(new_list, [0, 1, 2, 3, 4, 5, 7 ,8 ,9, 10])
