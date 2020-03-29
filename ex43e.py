"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

import itertools


def get_n_pandigitals_generator(n, include_zero=False):
    assert n < 10
    if include_zero:
        ini = 0
    else:
        ini = 1

    digits = []
    for i in range(ini, n+1):
        digits.append(str(i))
    return itertools.permutations(digits, len(digits))


def has_pandigit_exercise_property(pan_num_str):
    primes_for_ex = [2, 3, 5, 7, 11, 13, 17]
    len_of_substr = 3
    first_substring_start_index = 1
    assert (len(primes_for_ex) + len_of_substr) == len(pan_num_str)
    for index, prime in enumerate(primes_for_ex, first_substring_start_index):
        if int(pan_num_str[index: index + len_of_substr]) % prime != 0:
            return False
    return True


def get_sum_of_pandigital_nums_with_property(n, include_zero=False):
    pan_gen = get_n_pandigitals_generator(n, include_zero)
    pan_nums_with_property = []
    for pan_num in pan_gen:
        if pan_num[0] != 0:
            pan_num_str = "".join(pan_num)
            if has_pandigit_exercise_property(pan_num_str):
                pan_nums_with_property.append(int(pan_num_str))
    print(pan_nums_with_property)
    return sum(pan_nums_with_property)


# [1406357289, 1430952867, 1460357289, 4106357289, 4130952867, 4160357289]
# CPU times: user 5.15 s, sys: 35 µs, total: 5.15 s
# Wall time: 5.15 s
# 16695334890
