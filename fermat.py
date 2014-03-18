#Edward Schembor
#PrimalPy Package
#Fermat Primality Test

def fermatTest( testNum, checks ):
	"""Determines if a number is prime using the Fermat Primality test
	
	Parameters
	==========
	testNum : Integer
	          The number that will be tested for primality
	
	check : Integer
	        The number of times testNum will be compared with a random
			number for primality
			
    Returns
	=======
	successCount : The number of times that when checked with a random number, 
	testNum was determined to be prime
	
	References
	==========
	[1] http://en.wikipedia.org/wiki/Fermat_primality_test
	[2] http://en.wikipedia.org/wiki/Fermat%27s_little_theorem
	"""
	
	successCount = 0
	if checks <= testNum/10:
		checks = testNum/8
	for x in range(0, checks):
		a = random.randint(2, testNum-1)
		if (a**(testNum-1))%testNum == 1:
			successCount++;
		else:
			return False
	return successCount