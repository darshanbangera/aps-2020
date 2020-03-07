n = int(input())
bits = 0;
while(n):
    bits = bits + 1
    n = n & n-1
print(bits)
