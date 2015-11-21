import unittest

from ddt import ddt, data, unpack

from ..algorithms.insertion_sort import InsertionSort
from .test_cases import SortTestCases


TEST_TUPLES = SortTestCases.get_test_case_tuples()

@ddt
class InsertionSortTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_swap(self):
        swap_case = InsertionSort([10, 2, 3, 4, 5, 7, 8, 9, 0, 1])
        swap_case.swap(0, 1)
        self.assertEqual(swap_case.list, [2, 10, 3, 4, 5, 7, 8, 9, 0, 1])

    def test_bubble_last(self):
        list = [0, 1, 2, -1, 1]
        bubble_last_case = InsertionSort(list)
        bubble_last_case.bubbleLast(3)
        self.assertEqual(bubble_last_case.list, [-1, 0, 1, 2, 1])

    @data(TEST_TUPLES[0], TEST_TUPLES[1], TEST_TUPLES[2], TEST_TUPLES[3], 
        TEST_TUPLES[4], TEST_TUPLES[5], TEST_TUPLES[6])
    @unpack
    def test_all_sort_cases(self, input, expected):
        sort_object = InsertionSort(input)
        result = sort_object.sort()
        self.assertEqual(result, expected)
