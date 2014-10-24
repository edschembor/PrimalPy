#Edward Schembor
#PrimalPy Package
#Solovay-Strassen Primality Test

def solovay_strassen( test_num, test_count ):
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
    
    for int in range(0, test_count):
        a = random.randint(2, test_num-1)
        x = (a / test_num)
        p = a**((test_num-1)/2)
        if x == 0 or p != (x%test_num):
            return False
    return True 