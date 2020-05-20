import random
t = int(input())
while(t):
    n,m,k = map(int,input().split())
    for i in range(n):
        arr = list(map(int,input().split()))
    for i in range(n):
        print (random.randrange(1, m+1, 1),end=' ') 
    t =t-1
