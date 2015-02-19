# Edward Schembor
# PrimalPy Package
# Pocklington-Lehmer Primality Test

import math
from fractions import gcd
from get_prime_array import get_prime_array


def pocklington_lehmer(test_num):
    """Determines if a number is prime using the Pocklington-Lehmer Primality test
    Uses pre-generated primes to increase speed of the test.

    Parameters
    ==========
    test_num : Integer
              The number that will be tested for primality

    Returns
    =======
    boolean : Whether or not testNum is determined to be prime

    References
    ==========
    [1] http://en.wikipedia.org/wiki/Pocklington_primality_test
    """

    if (test_num <= 500000):
        # Use pre-generated primes
        prime_set = get_prime_array(test_num)

    for (q in prime_set):
        for (a in range(0, test_num)):
            if ((test_num - 1) % q == 0):
                if (((a**(test_num - 1)) % test_num) == 1):
                    if (gcd(a**((test_num - 1)/q)-1, test_num) == 1):
                        return True
    return False
