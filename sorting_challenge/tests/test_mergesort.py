import unittest

from ddt import ddt, data, unpack

from ..algorithms.merge_sort import MergeSort
from .test_cases import SortTestCases


TEST_TUPLES = SortTestCases.get_test_case_tuples()

@ddt
class MergeSortTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_merge(self):
        list = [5, 6, 7, 8, 1, 2, 3, 4]
        merge_case = MergeSort(list)
        merge_case.merge(0, 3, 7)
        self.assertEqual(merge_case.list, [1, 2, 3, 4, 5, 6, 7, 8])

    @data(TEST_TUPLES[0], TEST_TUPLES[1], TEST_TUPLES[2], TEST_TUPLES[3], 
        TEST_TUPLES[4], TEST_TUPLES[5], TEST_TUPLES[6])
    @unpack
    def test_all_sort_cases(self, input, expected):
        sort_object = MergeSort(input)
        result = sort_object.sort()
        self.assertEqual(result, expected)
