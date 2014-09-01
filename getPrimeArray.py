#Edward Schembor
#PrimalPy Package
#Pocklington-Lehmer Primality Test

def get_prime_array( high ):
    """Gets all primes lower than high from the pre-generated primes to improve efficiency
    
    Parameters
    ==========
    high : Integer
              The number below which primes will be returned
            
    Returns
    =======
    int array : The primes less than high
    """

    #Need to cleanse this to avoid repitition
    max_one_hundred_thousand = open("./pre_generated_primes/primes-to-100k.txt")
    one_hundred = max_one_hundred_thousand.readlines()
    max_one_hundred_thousand.close()

    if ( high > 100000 ):
        max_two_hundred_thousand = open("./pre_generated_primes/primes-to-200k.txt")
        two_hundred = max_two_hundred_thousand.readlines()
        max_two_hundred_thousand.close()

    if ( high > 200000 ):
        max_three_hundred_thousand = open("./pre_generated_primes/primes-to-300k.txt")
        three_hundred = max_three_hundred_thousand.readlines()
        max_three_hundred_thousand.close()

    if ( high > 300000 ):
        max_four_hundred_thousand = open("./pre_generated_primes/primes-to-400k.txt")
        four_hundred = max_four_hundred_thousand.readlines()
        max_four_hundred_thousand.close()

    if ( high > 500000 ):
        max_five_hundred_thousand = open("./pre_generated_primes/primes-to-500k.txt")
        five_hundred = max_five_hundred_thousand.readlines()
        max_five_hundred_thousand.close()