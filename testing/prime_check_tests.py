# Test Cases for PrimalPy

import unittest
from getPrimeArray.py import get_prime_array
from pocklington_lehmer.py import pocklington_lehmer

class TestGetPrimeArray(unittest.TestCase):

    def setUp(self):
        #Create a prime array using the get_prime_array method
        self.primeSet = get_prime_array( 250000 )
    
    def testCorrect(self):
        #Make sure general properties are correct
        self.assertEqual( len(self.primeSet), 22044 ) #Correct number from WolframAlpha
        self.assertEqual( self.primeSet[22043], 249989 )
        self.assertEqual( self.primeSet[0], 2 )

class TestPocklingtonLehmer(unittest.TestCase):

    def setUp(self):
        #Use the pre-generated primes to test the primality tests - we test with all primes <= 200000
        self.primeSet = get_prime_array(200000)
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