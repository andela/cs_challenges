import unittest

from ddt import ddt, data, unpack

from ..algorithms.selection_sort import SelectionSort
from .test_cases import SortTestCases


TEST_TUPLES = SortTestCases.get_test_case_tuples()

@ddt
class SelectionSortTests(unittest.TestCase):

    def setUp(self):
        self.sel_sort_obj = SelectionSort([0, 2, 3, 4, 5, 7, 8, 9, 10, 1])

    def test_swap(self):
        self.sel_sort_obj.swap(0, 1)
        self.assertEqual(self.sel_sort_obj.list, [2, 0, 3, 4, 5, 7, 8, 9, 10, 1])

    def test_find_min(self):
        min_index = self.sel_sort_obj.findMin(1)
        self.assertEqual(min_index, 9)


    @data(TEST_TUPLES[0], TEST_TUPLES[1], TEST_TUPLES[2], TEST_TUPLES[3], 
        TEST_TUPLES[4], TEST_TUPLES[5], TEST_TUPLES[6])
    @unpack
    def test_all_sort_cases(self, input, expected):
        sort_object = SelectionSort(input)
        result = sort_object.sort()
        self.assertEqual(result, expected)
