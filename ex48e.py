"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""


def self_powers(n):
    sum_self_powers = 0
    for i in range(1, n):
        sum_self_powers += i ** i
    return sum_self_powers


def get_last_n_digits_of_int(n, integer):
    str_of_int = str(integer)
    return str_of_int[len(str_of_int)-n:]


# CPU times: user 19 ms, sys: 0 ns, total: 19 ms
# Wall time: 18.6 ms
# '9110846700'
