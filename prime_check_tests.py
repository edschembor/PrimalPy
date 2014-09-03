# Test Cases for PrimalPy

import unittest
from getPrimeArray.py import get_prime_array
from pocklington_lehmer.py import pocklington_lehmer

class TestPocklingtonLehmer(unittest.TestCase):

    def setUp(self):
        #Use the pre-generated primes to test the primality tests - we test with all primes <= 500000
        self.primeSet = get_prime_array(500000)
        self.notPrimes = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]

    def test_true(self):
        for prime in self.primeSet:
            # Makes sure the test returns true for primes
            assertTrue( pocklington_lehmer( prime ) )
        for notPrime in self.notPrimes:
            # Makes sure the test returns false for non-primes
            assertFalse( pocklington_lehmer( notPrime ) )

if __name__ == '__main__':
    unittest.main()