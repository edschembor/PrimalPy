# Test Cases for PrimalPy

#TODO: - stop mixing camelCase and this_format
#      - move directory
#      - better way to test not primes - ie) test 2

import unittest
from getPrimeArray import get_prime_array
from pocklington_lehmer import pocklington_lehmer
from trialDivision import trial_division

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
        #Use the pre-generated primes to test - we test with all primes <= 200000
        self.primeSet = get_prime_array(200000)
        self.notPrimes = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]

    def test_true(self):
        # Makes sure the test returns true for primes
        for prime in self.primeSet:
            assertTrue( pocklington_lehmer( prime ) )

    def test_false(self):
        # Makes sure the test returns false for non-primes
        for notPrime in self.notPrimes:
            assertFalse( pocklington_lehmer( notPrime ) )

class TestTrialDivision(unittest.TestCase):
    
	def setUp(self):
        #Use the pre-generated primes to test - we test with all primes <= 200000
	    #TODO: don't do this in every test
	    self.primeSet = get_prime_array(200000)
        self.notPrimes = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]

    def test_true(self):
        # Makes sure the test returns true for primes
		for prime in self.primeSet:
            assertTrue( trial_division( prime ) )

    def test_false(self):
	    #Makes sure the test returns false for non-primes
	    for notPrime in self.notPrimes:
		    assertFalse( trial_division( prime ) )
			
if __name__ == '__main__':
    unittest.main()