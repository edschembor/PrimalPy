# Edward Schembor
# PrimalPy Package
# Pocklington-Lehmer Primality Test


def get_prime_array(high):
    """Gets all primes lower than high from the pre-generated primes to
    improve efficiency.

    Parameters
    ==========
    high : Integer
              The number below which primes will be returned

    Returns
    =======
    int array : The primes less than high
    """

    # Array of pre-generated primes less than high
    primes = []

    with open("../pre_generated_primes/primes-to-100k.txt") as f:
        for line in f:
            hundred = [int(i) for i in line.split()]
            primes.extend(hundred)

    if (high > 100000):
        with open("../pre_generated_primes/primes-to-200k.txt") as f2:
            for line in f2:
                two_hundred = [int(i) for i in line.split()]
                primes.extend(two_hundred)

    if (high > 200000):
        with open("../pre_generated_primes/primes-to-300k.txt") as f:
            for line in f:
                three_hundred = [int(i) for i in line.split()]
                primes.extend(three_hundred)

    if (high > 300000):
        with open("../pre_generated_primes/primes-to-400k.txt") as f:
            for line in f:
                four_hundred = [int(i) for i in line.split()]
                primes.extend(four_hundred)

    if (high > 400000):
        with open("../pre_generated_primes/primes-to-500k.txt") as f:
            for line in f:
                five_hundred = [int(i) for i in line.split()]
                primes.extend(five_hundred)

    for x in reversed(range(0, len(primes))):
        if primes[x] > high:
            primes.pop(x)
        else:
            break

    return primes
