class SortTestCases:
    
    input = {
        'pre_sorted_forwards' : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        'pre_sorted_backwards' : [9, 8, 7, 6, 5, 4, 3, 2, 1],

        'even_length' : [4, 21, 6, 7, 0, 1, 10, 9],
        'odd_length' : [4, 21, 6, 7, 0, 1, 10, 9, 25],

        'first_half_sorted' : [0, 1, 2, 3, 4, 23, 89, 19, 12, 20],
        'second_half_sorted' : [23, 89, 19, 12, 20, 0, 1, 2, 3, 4],

        'random_list' : [10, 2, 3, 4, 5, 7, 8, 9, 0, 1]
    }

    expected_results = {
        'pre_sorted_forwards' : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        'pre_sorted_backwards' : [1, 2, 3, 4, 5, 6, 7, 8, 9],

        'even_length' : [0, 1, 4, 6, 7, 9, 10, 21],
        'odd_length' : [0, 1, 4, 6, 7, 9, 10, 21, 25],

        'first_half_sorted' : [0, 1, 2, 3, 4, 12, 19, 20, 23, 89],
        'second_half_sorted' : [0, 1, 2, 3, 4, 12, 19, 20, 23, 89],

        'random_list' :  [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
    }

    tuples = (
        (input['pre_sorted_forwards'], expected_results['pre_sorted_forwards']),
        (input['pre_sorted_backwards'], expected_results['pre_sorted_backwards']),
        (input['even_length'], expected_results['even_length']),
        (input['odd_length'], expected_results['odd_length']),
        (input['first_half_sorted'], expected_results['first_half_sorted']),
        (input['second_half_sorted'], expected_results['second_half_sorted']),
        (input['random_list'], expected_results['random_list'])
    )

    @classmethod
    def get_test_case_tuples(cls):
        return cls.tuples;
