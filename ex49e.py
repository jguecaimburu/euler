"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.
There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?

"""

from euler_snippets import get_primes_in


def get_primes_that_match_problem_conditions():
    four_digit_primes = [p for p in get_primes_in(10000) if p > 999]
    primes_grouped_by_digits = group_numbers_by_permutations(four_digit_primes)
    answers = []
    for sort_id, primes_list in primes_grouped_by_digits.items():
        if len(primes_list) >= 3:
            answer = get_equidistance_numbers_from_list(primes_list, 3)
            if answer:
                answers.append(answer)
    return answers


def group_numbers_by_permutations(list_of_int):
    groups_dict = {}
    for i in list_of_int:
        i_sorted_digits = sort_number_digits(i)
        if i_sorted_digits not in groups_dict.keys():
            groups_dict[i_sorted_digits] = []
        groups_dict[i_sorted_digits].append(i)
    return groups_dict


def sort_number_digits(integer):
    return "".join(sorted([i for i in str(integer)]))


def get_equidistance_numbers_from_list(list_of_int, min_sequence_len):
    distance_dict = get_distance_dict(list_of_int)
    for equidistance_list in distance_dict.values():
        if len(equidistance_list) >= min_sequence_len - 1:
            consecutive_pairs = get_consecutive_pairs(equidistance_list)
            for list_of_consecutives in consecutive_pairs.values():
                if len(set(list_of_consecutives)) >= min_sequence_len:
                    return set(list_of_consecutives)
    return None


def get_distance_dict(list_of_int):
    sorted_list = sorted(list_of_int)
    distance_dict = {}
    for index, integer in enumerate(sorted_list[:-1]):
        for higher_index in range(index + 1, len(sorted_list)):
            distance = sorted_list[higher_index] - integer
            if distance not in distance_dict.keys():
                distance_dict[distance] = []
            distance_dict[distance].append((integer,
                                            sorted_list[higher_index]))
    return distance_dict


def get_consecutive_pairs(equidistance_list):
    consecutive_pairs = {}
    last_was_consecutive = False
    for index, tuple in enumerate(equidistance_list[:-1]):
        if tuple[1] == equidistance_list[index+1][0]:
            if not last_was_consecutive:
                last_was_consecutive = True
                first_tuple_in_seq = tuple
                accum_tuple = tuple + equidistance_list[index+1]
            else:
                accum_tuple += equidistance_list[index+1]
            if index == len(equidistance_list) - 2:
                consecutive_pairs[first_tuple_in_seq] = accum_tuple
        else:
            if last_was_consecutive:
                last_was_consecutive = False
                consecutive_pairs[first_tuple_in_seq] = accum_tuple
    return consecutive_pairs


# CPU times: user 8.76 ms, sys: 0 ns, total: 8.76 ms
# Wall time: 9.82 ms
# [{1487, 4817, 8147}, {2969, 6299, 9629}]
