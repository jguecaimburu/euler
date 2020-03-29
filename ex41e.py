"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""

import numpy as np
import time


def get_max_pan_prime(fragmentation=1):
    start_time = time.time()
    limit = 10 ** 9
    primes_in_limit = get_primes_in_big_limit(limit, fragmentation)
    print("Got all primes in", time.time() - start_time, "seconds")
    for p in primes_in_limit[::-1]:
        if are_all_digits_different_and_not_zero(str(p)):
            if is_num_pan(str(p)):
                return p


def are_all_digits_different_and_not_zero(string):
    for s in string:
        if string.count(s) != 1 or s == '0':
            return False
    return True


def is_num_pan(string):
    pan_range = range(1, len(string) + 1)
    for n in pan_range:
        if str(n) not in string:
            return False
    return True


def get_primes_in_big_limit(limit, fragmentation=1):
    """Takes a big limit as an integer and get all the prime numbers in that
    range, including the limit itself. Returns a numpy array of the primes.
    Fragmentation is an int that multiplies the sqrt of the limit to increase
    the fragment size. Consumes more memory and less time.
    Fragmentation limit = sqrt of limit
    For 4 GB RAM not enough memory for limit == 10**9
    """
    print("Getting primes...")
    print("Fragmentation set to", fragmentation)
    fragment_limit = int(np.sqrt(limit))
    fragment_lowest = 0
    fragment_highest = fragment_lowest + fragment_limit
    primes_in_limit = np.array([], dtype=int)
    while fragment_highest < limit:
        if fragment_lowest == 0:
            fragment_highest += 1
            primes_in_first_fragment = get_primes_in(fragment_highest)
            primes_in_limit = np.concatenate([primes_in_limit,
                                             primes_in_first_fragment],
                                             axis=None)
        else:
            primes_in_fragment = get_primes_in_fragment(fragment_lowest,
                                                        fragment_highest,
                                                        primes_in_first_fragment
                                                        )
            primes_in_limit = np.concatenate([primes_in_limit,
                                             primes_in_fragment],
                                             axis=None)
        fragment_lowest = fragment_highest
        fragment_highest += (fragment_limit * fragmentation)
    primes_in_last_fragment = get_primes_in_fragment(fragment_lowest,
                                                     limit+1,
                                                     primes_in_first_fragment
                                                     )
    return np.concatenate([primes_in_limit, primes_in_last_fragment], axis=None)


def get_primes_in(limit):
    """Takes a limit as an integer and get all the prime numbers in that range,
    NOT including the limit itself. Returns a numpy array of the primes.
    """
    range_limit = np.arange(limit)
    prime_mask = np.ones(limit, dtype=bool)
    prime_mask[0:2] = False
    for i in range_limit[:int(np.sqrt(limit))+1]:
        if prime_mask[i]:
            prime_mask[2*i::i] = False
    return range_limit[prime_mask]


def get_primes_in_fragment(fragment_lowest, fragment_highest,
                           primes_in_first_fragment):
    """Takes fragment lowest and highest limits as an integers and get all the
    prime numbers in that range, NOT including the limit itself. Returns a
    numpy array of the primes. Needs the primes from the first fragment of the
    program as input.
    """
    fragment_range = np.arange(fragment_lowest, fragment_highest)
    prime_mask = np.ones(len(fragment_range), dtype=bool)
    for p in primes_in_first_fragment:
        if fragment_lowest % p == 0:
            first_multiple = fragment_lowest // p
        else:
            first_multiple = fragment_lowest // p + 1
        first_multiple_index = first_multiple * p - fragment_lowest
        prime_mask[first_multiple_index::p] = False
    return fragment_range[prime_mask]


# Getting primes...
# Fragmentation set to 1000
# Got all primes in 23.722146034240723 seconds
# CPU times: user 1min 33s, sys: 7.31 s, total: 1min 41s
# Wall time: 1min 32s
# 7652413
