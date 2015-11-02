import unittest

from ..algorithms.merge_sort import MergeSort
from nose.tools import set_trace


class MergeSortTests(unittest.TestCase):

    def setUp(self):
        self.obj = MergeSort([10, 2, 3, 4, 5, 7, 8, 9, 0, 1])


    def test_merge(self):
        list = [5, 6, 7, 8, 1, 2, 3, 4]
        obj = MergeSort(list)
        obj.merge(0, 3, 7)
        self.assertEqual(obj.list, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_sorted(self):
        new_list = self.obj.sort()
        self.assertEqual(new_list, [0, 1, 2, 3, 4, 5, 7 ,8 ,9, 10])
