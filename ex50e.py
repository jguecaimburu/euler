"""
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below
one-hundred.
The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

from euler_snippets import get_primes_in
import itertools


def get_prime_with_longer_consecutive_below(limit):
    primes = get_primes_in(limit)
    biggest_sum_chain = 0
    prime_with_longer_chain = None
    for i in range(len(primes)):
        accumulate = [accum for accum in itertools.accumulate(primes[i:])
                      if (accum < limit)]
        if len(accumulate) < biggest_sum_chain:
            return prime_with_longer_chain, biggest_sum_chain
        for len_of_chain, sum_of_primes in enumerate(accumulate, 1):
            if sum_of_primes % 2 != 0 and sum_of_primes in primes:
                if len_of_chain > biggest_sum_chain:
                    biggest_sum_chain = len_of_chain
                    prime_with_longer_chain = sum_of_primes


# CPU times: user 172 ms, sys: 9.88 ms, total: 181 ms
# Wall time: 183 ms
# (997651, 543)
