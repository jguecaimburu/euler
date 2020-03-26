"""
It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.
9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12
It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?
"""

from euler_snippets import get_primes_in_big_limit
import numpy as np


class BreakGoldbach():
    def __init__(self, primes_limit, square_limit):
        self.primes_limit = primes_limit
        self.square_limit = square_limit

    def set_primes_in_limit(self):
        self.primes = list(get_primes_in_big_limit(self.primes_limit,
                                                   fragmentation=1000))
        print("Primes set from %d to %d"
              % (self.primes[0], self.primes[-1]))

    def set_double_of_square_list(self):
        def double_sq(int):
            return 2 * (int ** 2)
        square_range = list(range(1, self.square_limit))
        self.double_sq = list(map(double_sq, square_range))
        print("Double squares set from %d to %d"
              % (self.double_sq[0], self.double_sq[-1]))

    def sum_primes_and_squares(self):
        array_of_primes = np.array(self.primes).reshape((len(self.primes), 1))
        transposed_squares = np.array(self.double_sq) \
            .reshape(1, (len(self.double_sq)))
        sum_of_elements = array_of_primes + transposed_squares
        self.sum = sorted(np.unique(sum_of_elements))
        print("Sum of arrays done.")

    def get_answer(self):
        prime_gen = (p for p in self.primes)
        sum_gen = (s for s in self.sum)
        prime = 0
        sum_int = 0
        for odd in range(3, self.primes_limit, 2):
            while prime < odd:
                prime = next(prime_gen)
            if prime != odd:
                while sum_int < odd:
                    sum_int = next(sum_gen)
                if sum_int != odd:
                    return odd

    def break_goldbach(self):
        self.set_primes_in_limit()
        self.set_double_of_square_list()
        self.sum_primes_and_squares()
        return self.get_answer()

# Getting primes...
# Fragmentation set to 1000
# Primes set from 2 to 99991
# Double squares set from 2 to 1996002
# Sum of arrays done.
# CPU times: user 1.35 s, sys: 202 ms, total: 1.56 s
# Wall time: 1.46 s
# 5777
# Sum of arrays breaks memory for big input
