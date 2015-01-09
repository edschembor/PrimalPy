# Test Cases for PrimalPy

import unittest
import sys
sys.path.insert(0, '../')


from get_prime_array import get_prime_array
from pocklington_lehmer import pocklington_lehmer
from trial_division import trial_division


class TestGetPrimeArray(unittest.TestCase):

    def setUp(self):
        #Create a prime array using the get_prime_array method
        self.prime_set = get_prime_array( 250000 )
    
    def test_correct(self):
        #Make sure general properties are correct
        self.assertEqual( len(self.prime_set), 22044 )
        self.assertEqual( self.prime_set[22043], 249989 )
        self.assertEqual( self.prime_set[0], 2 )

class TestTrialDivision(unittest.TestCase):
    
    def setUp(self):
        #Use the pre-generated primes to test - we test with all primes <= 200000
        #TODO: don't do this in every test
        self.prime_set = get_prime_array(200000)
        self.not_primes = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]

    def test_true(self):
        # Makes sure the test returns true for primes
        for prime in self.prime_set:
            self.assertTrue( trial_division( prime ) )

    def test_false(self):
        #Makes sure the test returns false for non-primes
        for notPrime in self.not_primes:
            self.assertFalse( trial_division( notPrime ) )

if __name__ == '__main__':
    unittest.main()