#Edward Schembor
#PrimalPy Package
#Trial Division Primality Test

def trial_division( test_num ):
   """Determines if a number is prime using the most basic test of trial division
    
    Parameters
    ==========
    test_num : Integer
    The number that will be tested for primality
            
    Returns
    =======
    boolean : Whether or not testNum is determined to be prime
    
    References
    ==========
    [1] http://en.wikipedia.org/wiki/Trial_division
    """
    
    if test_num < 2:
        return False
    if test_num in (2, 3):
        return True
    if test_num % 2 == 0 or test_num % 3 == 0:
        return False
    max_divisor = int(test_num ** 0.5) 
    divisor = 5
    while divisor <= max_divisor:
        if test_num % divisor == 0 or test_num % (divisor + 2) == 0:
            return False
        divisor += 6
    return True