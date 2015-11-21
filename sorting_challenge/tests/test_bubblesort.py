import unittest

from ddt import ddt, data, unpack

from ..algorithms.bubble_sort import BubbleSort
from .test_cases import SortTestCases


TEST_TUPLES = SortTestCases.get_test_case_tuples()

@ddt
class BubbleSortTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_swap(self):
        swap_case = BubbleSort([10, 2, 3, 4, 5, 7, 8, 9, 0, 1])
        swap_case.swap(0, 1)
        self.assertEqual(swap_case.list, [2, 10, 3, 4, 5, 7, 8, 9, 0, 1])

    
    @data(TEST_TUPLES[0], TEST_TUPLES[1], TEST_TUPLES[2], TEST_TUPLES[3], 
        TEST_TUPLES[4], TEST_TUPLES[5], TEST_TUPLES[6])
    @unpack
    def test_all_sort_cases(self, input, expected):
        sort_object = BubbleSort(input)
        result = sort_object.sort()
        self.assertEqual(result, expected)
