#Edward Schembor
#PrimalPy Package
#Solovay-Strassen Primality Test

def solovay_strassen( testNum, testCount ):
"""Determines if a number is prime using the Miller-Rabin Primality test
    
    Parameters
    ==========
    testNum : Integer
              The number that will be tested for primality
    
    testCount : Integer
            The number of times testNum will be compared with a random
            number for primality
            
    Returns
    =======
    boolean : Whether or not testNum is determined to be prime
    
    References
    ==========
    [1] http://en.wikipedia.org/wiki/Solovay%E2%80%93Strassen_primality_test
    """
    
    for int in range(0, testCount):
        a = random.randint(2, testNum-1)
        x = (a / testNum)
        p = a**((testNum-1)/2)
        if x == 0 or p != (x%testNum):
            return False
    return True 