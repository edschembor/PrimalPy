#Edward Schembor
#PrimalPy Package
#Pocklington-Lehmer Primality Test

import math
from fractions import gcd
from get_prime_array import get_prime_array

def pocklington_lehmer( test_num ):
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

    if ( test_num <= 500000 ):
        # Use pre-generated primes
        prime_set = get_prime_array(test_num)
        print prime_set

    for q in prime_set:
        for a in range(0, 500000):
            if ( (test_num - 1)%q != 0 ):
                print "111"
                break
            if ( (a**(test_num - 1)) % test_num != 1 % test_num ):
                print "222"
                break
            if (gcd(a**((test_num - 1)/q)-1, test_num) != 1):
                print "333"
                break
            return True
    return False 
