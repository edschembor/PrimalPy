#Edward Schembor
#PrimalPy Package
#Solovay-Strassen Primality Test

#A probabalistic primality test
#Also acts as a compositeness test

def solovay_strassen( testNum, accuracy ):
	for int in range(0, accuracy):
		a = random.randint(2, testNum-1)
		x = (a / testNum)
		p = a**((testNum-1)/2)
		if x == 0 or p != (x%testNum):
			return False
	return True 