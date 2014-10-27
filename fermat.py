#Edward Schembor
#PrimalPy Package
#Fermat Primality Test

import random

def fermat_test( test_num, test_count ):
    """Determines if a number is prime using the Fermat Primality test
    
    Parameters
    ==========
    test_num : Integer
              The number that will be tested for primality
    
    test_count : Integer
            The number of times testNum will be compared with a random
            number for primality
            
    Returns
    =======
    success_count : The number of times that when checked with a random number, 
    test_num was determined to be prime
    
    References
    ==========
    [1] http://en.wikipedia.org/wiki/Fermat_primality_test
    [2] http://en.wikipedia.org/wiki/Fermat%27s_little_theorem
    """
    
    success_count = 0
    if test_count <= test_num/10:
        test_count = test_num/8
    for x in range(0, test_count):
        a = random.randint(2, test_num-1)
        if (a**(test_num-1))%test_num == 1:
            success_count += 1
        else:
            return False
    return success_count
