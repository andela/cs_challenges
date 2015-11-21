import unittest

from ddt import ddt, data, unpack

from ..algorithms.quick_sort import QuickSort
from .test_cases import SortTestCases


TEST_TUPLES = SortTestCases.get_test_case_tuples()

@ddt
class QuickSortTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_swap(self):
        swap_case = QuickSort([10, 2, 3, 4, 5, 7, 8, 9, 0, 1])
        swap_case.swap(0, 1)
        self.assertEqual(swap_case.list, [2, 10, 3, 4, 5, 7, 8, 9, 0, 1])

    def test_partition(self):
        list = [12, 7, 14, 9, 10, 11]
        partition_case = QuickSort(list)
        pivot = partition_case.partition(0, 5)
        self.assertEqual(pivot, 3)
        self.assertEqual(partition_case.list[pivot], 11)
        self.assertEqual(partition_case.list, [7, 9, 10, 11, 14, 12])

    @data(TEST_TUPLES[0], TEST_TUPLES[1], TEST_TUPLES[2], TEST_TUPLES[3], 
        TEST_TUPLES[4], TEST_TUPLES[5], TEST_TUPLES[6])
    @unpack
    def test_all_sort_cases(self, input, expected):
        sort_object = QuickSort(input)
        result = sort_object.sort()
        self.assertEqual(result, expected)
