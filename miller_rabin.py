#Edward Schembor
#PrimalPy Package
#Miller-Rabin Primality Test


def modulo(a,b,c):
        x = 1
        y = a
        while (b > 0):
                if (b % 2) == 1:
                        x = (x * y) % c
                y = (y * y) % c
                b = b / 2
        return x % c
         
def millerRabin(testNum, testCount):
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
    [1] http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    """

        if testNum < 2:
                return False
        if testNum != 2 and testNum%2 == 0:
                return False
         
        d = testNum-1
        while d % 2 == 0:
                d = d / 2
         
        for i in range(testCount):
                a = random.randint(1, testNum-1)
                temp = d
                x = modulo(a, temp, testNum)
                while temp!=testNum-1 and x!=1 and x!=testNum-1:
                        x = (x * x) % testNum
                        temp = temp * 2
                 
                if x != testNum-1 and temp%2 == 0:
                        return False
         
        return True