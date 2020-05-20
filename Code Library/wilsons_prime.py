import math

def isPrime(n):
	return math.factorial(n-1)%n == n-1

print(isPrime(17))
