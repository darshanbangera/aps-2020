import math

def armstrong(n):
	c = n
	d = math.floor(math.log10(c)+1)
	s = 0
	while(n):
		s+=(n%10)**d
		n//=10
	if s == c:
		return True
	return False 

n = 1634
print(armstrong(n))
