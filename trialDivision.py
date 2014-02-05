#Edward Schembor
#PrimalPy Package
#Trial Division Primality Test

def trialDivision( testNum ):
    if testNum < 2:
        return False
    if testNum in (2, 3):
        return True
    if testNum % 2 == 0 or testNum % 3 == 0:
        return False
    max_divisor = int(testNum ** 0.5) 
    divisor = 5
    while divisor <= max_divisor:
        if testNum % divisor == 0 or testNum % (divisor + 2) == 0:
            return False
        divisor += 6
    return True