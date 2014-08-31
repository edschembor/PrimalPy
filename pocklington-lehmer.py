#Edward Schembor
#PrimalPy Package
#Pocklington-Lehmer Primality Test

from fractions import gcd

def pocklington_lehmer( testNum ):
    """Determines if a number is prime using the Pocklington-Lehmer Primality test
    
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

    #Generate a prime q such that q < sqrt(n) - 1 and a number a
    q = 2
	a = 2

    if ( (testNum - 1)%q == 0):
        return True
    else:
        return False

    if ( (a**(testNum - 1))%testNum == 1%testNum ):
        return True
    else:
        return False
	
    if (gcd(a**((testNum - 1)/q)-1, testNum) == 1):
	    return True
    else:
        return False 