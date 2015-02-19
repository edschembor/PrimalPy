# Edward Schembor
# PrimalPy Package
# Solovay-Strassen Primality Test

import random


def legendre(a, p):
    """Determins the Legendre symbol of a and p

    Parameters
    ==========
    a : A quadratic residue modulo p if it is congruent to a perfect
        square modulo p, else it is a quadratic nonresidue modulo p

    p : An odd prime number

    Returns
    =======
    int : The Legendre Symbol of the two inputs

    References
    ==========
    [1] http://en.wikipedia.org/wiki/Legendre_symbol
    """

    if(p < 2):
        raise InputError('p must be greater than 2')
    if(a == 0) or (a == 1):
        return a
    if(a % 2 == 0):
        re = legendre(a / 2, p)
        if(p * p - 1 & 8 != 0):
            re *= -1
    else:
        re = legendre(p % a, a)
        if((a - 1) * (p - 1) & 4 != 0):
            re *= -1
    return re


def solovay_strassen(test_num, test_count):
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
    [1] http://en.wikipedia.org/wiki/Solovay%E2%80%93Strassen_primality_test
    """

    if(test_num == 2 or test_num == 3):
        return True

    for int in range(0, test_count):
        a = random.randrange(2, test_num-1)
        x = legendre(a, test_num)
        p = pow(a, (test_num-1) / 2, test_num)
        if x == 0 or p != (x % test_num):
            return False
    return True
