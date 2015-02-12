#Edward Schembor
#PrimalPy Package
#Prime Generation
#Trial Division Generation

import sys
sys.path.insert(0, '../')
from get_prime_array import get_prime_array
from trial_division import trial_division

def trial_division_generation( num_primes ):
    if( num_primes <= 500000 ):
        #Use the pre-generated primes
        prime_set = get_prime_array(num_primes)
        return prime_set
    else:
        prime_set = get_prime_array(num_primes)
        current = 500001
        while(current <= num_primes):
            if(trial_division(current)):
                prime_set.append(current)
            current = current + 1
        return prime_set