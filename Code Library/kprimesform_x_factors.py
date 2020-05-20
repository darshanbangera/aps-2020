import math

t = int(input())
for _ in range(t):
    x,k = map(int,input().split())
    ct = 0
    i = 2
    while(1):
        if x%i==0:
            x=x//i
            ct+=1
            i=2
        else:
            i+=1
        if x==1 or i>math.sqrt(x):
            break
    if x!=1:
        ct+=1
    if ct<k:
        print(0)
    else:
        print(1)
