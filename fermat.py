#Edward Schembor
#PrimalPy Package
#Fermat Primality Test

#Fermat's probabalistic primality test

def fermatTest( testNum, checks ):
	successCount = 0
	if( checks <= testNum/10 ):
		checks = testNum/8
	for x in range(0, checks):
		a = random.randint(2, testNum-1)
		if( (a**(testNum-1))%testNum == 1):
			successCount++;
		else:
			return False
	return successCount