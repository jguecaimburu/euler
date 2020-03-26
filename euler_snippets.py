"""
This file includes different snippets that were originally written to solve
a particular problem and then were useful for others as I move forward.
"""

import numpy as np


def get_primes_in_big_limit(limit, fragmentation=1):
    """Takes a big limit as an integer and get all the prime numbers in that
    range, including the limit itself. Returns a numpy array of the primes.
    Fragmentation is an int that multiplies the sqrt of the limit to increase
    the fragment size. Bigger fragmentation consumes more memory and less time.
    Fragmentation limit = sqrt of limit.
    For 4 GB RAM not enough memory for limit == 10**9. Fragmentation 1000 ok
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


def long_division(dividend_divisor_tuple, decimal_limit=5):
    """Takes a tuple where the first element is the dividend and the second
    element is the divisor. Both element sould be int. Performs a long division
    until it reaches one of the following conditions:
    - rest of division = 0 : Terminating
    - recurring cycle found
    - decimal precision reached
    Returns a tuple of the natural, decimal and recurring part. If one of these
    is not part of the result, it will be equal to None.
    """

    natural, decimal = [], []
    dividend, divisor = dividend_divisor_tuple[0], dividend_divisor_tuple[1]
    assert isinstance(dividend, int), "Dividend not int"
    assert isinstance(divisor, int), "Divisor not int"
    floor_div = dividend // divisor
    rest = dividend % divisor

    # Natural part of the division
    while floor_div > 0:
        natural.append(str(floor_div))
        dividend = rest
        floor_div = dividend // divisor
        rest = dividend % divisor
        if rest == 0:  # Divisor is factor of dividend
            print("Divisor is factor of dividend")
            return ("".join(natural), None, None)

    # Decimal part of the division
    dividend_list = []
    recurring_index = None
    while len(decimal) < decimal_limit:
        dividend_list.append(dividend)
        dividend *= 10
        floor_div = dividend // divisor
        decimal.append(str(floor_div))
        rest = dividend % divisor
        if rest == 0:  # Terminating decimal reached
            return ("".join(natural), "".join(decimal), None)
        elif rest in dividend_list:  # Recurring cycle found
            recurring_index = dividend_list.index(rest)
            print("Recurring cycle found")
            break
        else:
            dividend = rest

    if recurring_index is not None:
        recurring = decimal[recurring_index:]
        decimal = decimal[:recurring_index]
        return ("".join(natural), "".join(decimal), "".join(recurring))
    else:
        print("Decimal limit reached")
        return ("".join(natural), "".join(decimal), None)


def get_fibonacci_number():
    """Fibonacci number generator."""
    fibonacci_minus_2 = 1
    fibonacci_minus_1 = 1
    yield fibonacci_minus_2
    yield fibonacci_minus_1
    while True:
        fibonacci_n = fibonacci_minus_2 + fibonacci_minus_1
        yield fibonacci_n
        fibonacci_minus_2, fibonacci_minus_1 = fibonacci_minus_1, fibonacci_n


def get_number_length(number):
    """Get length of number in digits."""
    return len(str(number))


def cross_sum_elements_of_list(list_of_int):
    """ Returns array of all the posible sums between list elements."""
    array_of_int = np.array(list_of_int).reshape((len(list_of_int), 1))
    transposed_array = array_of_int.copy().T
    sum_of_elements_array = array_of_int + transposed_array
    return np.unique(sum_of_elements_array)


def get_divisors(num):
    """ Return list of all the divisors of an integer num."""
    assert num != 0, "Num is 0"
    divisors = []
    sq_root = int(num**0.5)
    for i in range(1, sq_root + 1):
        if num % i == 0:
            divisors.extend([i, num // i])
    # if num has a perfect sq, that number will be added twice, then:
    if sq_root ** 2 == num:
        divisors.remove(sq_root)
    return divisors
