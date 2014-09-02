#Edward Schembor
#PrimalPy Package
#Pocklington-Lehmer Primality Test

from fractions import gcd
from getPrimeArray.py import get_prime_array

def pocklington_lehmer( testNum ):
    """Determines if a number is prime using the Pocklington-Lehmer Primality test
    Uses pre-generated primes to increase speed of the test.
    
    Parameters
    ==========
    testNum : Integer
              The number that will be tested for primality
            
    Returns
    =======
    boolean : Whether or not testNum is determined to be prime
    
    References
    ==========
    [1] http://en.wikipedia.org/wiki/Pocklington_primality_test
    """

    #Generate a prime q such that q < sqrt(n) - 1
	high = math.sqrt(testNum) - 1
    if ( testNum <= 500000 ):
        # Use pre-generated primes
        primeSet = get_prime_array(high)
    else:
        # Generate primes
        primeSet = [2, 3, 5, 7, 11]

    for q in primeSet:
        for a in range(0, 100):
            if ( (testNum - 1)%q != 0):
                break

            if ( (a**(testNum - 1))%testNum != 1%testNum ):
                break
	
            if (gcd(a**((testNum - 1)/q)-1, testNum) != 1):
	            break

            return True
    return False 
