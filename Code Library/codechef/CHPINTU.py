t = int(input())
while(t):
    n,m = map(int,input().split())
    baskets = list(map(int,input().split()))
    val = list(map(int,input().split()))
    res = [0]*m
    for i in range(n):
        res[baskets[i]-1] += val[i]
    for i in range(1,m+1):
        if (i not in baskets):
            res[i-1] = 9999999999
    print(min(res))
    t-=1
