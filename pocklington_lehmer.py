#Edward Schembor
#PrimalPy Package
#Pocklington-Lehmer Primality Test

from fractions import gcd
from getPrimeArray import get_prime_array

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

    #Generate a prime q such that q < sqrt(n) - 1
    high = math.sqrt(test_num) - 1
    if ( test_num <= 500000 ):
        # Use pre-generated primes
        prime_set = get_prime_array(high)
    else:
        # Generate primes
        prime_set = [2, 3, 5, 7, 11]

    for q in prime_set:
        for a in range(0, 100):
            if ( (test_num - 1)%q != 0):
                break

            if ( (a**(test_num - 1))%test_num != 1%test_num ):
                break
	
            if (gcd(a**((test_num - 1)/q)-1, test_num) != 1):
	            break

            return True
    return False 
