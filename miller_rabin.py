# Edward Schembor
# PrimalPy Package
# Miller-Rabin Primality Test

import random


def miller_rabin(test_num, test_count):
    """Determines if a number is prime using the Miller-Rabin Primality test

    Parameters
    ==========
    test_num : Integer
              The number that will be tested for primality

    test_count : Integer
            The number of times testNum will be compared with a random
            number for primality

    Returns
    =======
    boolean : Whether or not testNum is determined to be prime

    References
    ==========
    [1] http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    """

    if test_num < 2:
            return False
    if test_num != 2 and test_num % 2 == 0:
            return False

    d = test_num-1
    while d % 2 == 0:
            d = d / 2

    for i in range(test_count):
            a = random.randint(1, test_num-1)
            temp = d
            x = pow(a, temp, test_num)
            while temp != test_num-1 and x != 1 and x != test_num-1:
                    x = (x * x) % test_num
                    temp = temp * 2

            if x != test_num-1 and temp % 2 == 0:
                    return False

    return True
