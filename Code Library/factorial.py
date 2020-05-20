def factorial(n):
	product = 1
	for i in range(2,n+1):
		product *= i
	return product

a = 10
print(factorial(a))
