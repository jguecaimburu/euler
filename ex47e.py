"""
The first two consecutive numbers to have two distinct prime factors are:
14 = 2 × 7
15 = 3 × 5
The first three consecutive numbers to have three distinct prime factors are:
644 = 2^2 × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors
each. What is the first of these numbers?
"""

import numpy as np


def get_ints_with_n_prime_factors_in(n, limit):
    range_limit = np.arange(limit)
    prime_mask = np.ones(limit, dtype=bool)
    count_array = np.zeros(limit, dtype=int)
    prime_mask[0:2] = False
    for i in range_limit[:int(np.sqrt(limit))+1]:
        if prime_mask[i]:
            prime_mask[2*i::i] = False
            count_array[i::i] += 1
    count_mask = count_array >= n
    return range_limit[count_mask]


def find_n_consecutive_nums_in_list(n, list_of_int):
    answer = []
    for index, num in enumerate(list_of_int[:-n]):
        for i in range(n):
            if list_of_int[index + i] != (num + i):
                break
        else:
            for i in range(n):
                answer.append(list_of_int[index+i])
    return answer


# CPU times: user 121 ms, sys: 0 ns, total: 121 ms
# Wall time: 122 ms
# [134043,
#  134044,
#  134045,
#  134046,
#  238203,
#  238204,
#  238205,
#  238206,
#  253894,
#  253895,
#  253896,
#  253897,
#  259368,
#  259369,
#  259370,
#  259371,
#  332994,
#  332995,
#  332996,
#  332997,
#  342054,
#  342055,
#  342056,
#  342057,
#  355508,
#  355509,
#  355510,
#  355511,
#  357642,
#  357643,
#  357644,
#  357645,
#  357643,
#  357644,
#  357645,
#  357646,
#  385032,
#  385033,
#  385034,
#  385035,
#  401554,
#  401555,
#  401556,
#  401557,
#  422094,
#  422095,
#  422096,
#  422097,
#  438954,
#  438955,
#  438956,
#  438957,
#  452352,
#  452353,
#  452354,
#  452355,
#  468753,
#  468754,
#  468755,
#  468756,
#  495649,
#  495650,
#  495651,
#  495652]
