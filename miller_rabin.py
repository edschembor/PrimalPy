#Edward Schembor
#PrimalPy Package
#Miller-Rabin Primality Test

#A probabalistic primality test

def modulo(a,b,c):
        x = 1
        y = a
        while (b > 0):
                if (b % 2) == 1:
                        x = (x * y) % c
                y = (y * y) % c
                b = b / 2
        return x % c
         
def millerRabin(testNum, accuracy):
        if testNum < 2:
                return False
        if testNum != 2 and testNum%2 == 0:
                return False
         
        d = testNum-1
        while d % 2 == 0:
                d = d / 2
         
        for i in range(accuracy):
                a = random.randint(1, testNum-1)
                temp = d
                x = modulo(a, temp, testNum)
                while temp!=testNum-1 and x!=1 and x!=testNum-1:
                        x = (x * x) % testNum
                        temp = temp * 2
                 
                if x != testNum-1 and temp%2 == 0:
                        return False
         
        return True