t = int(input())
for i in range(t):
    x,y,k,n = map(int,input().strip().split())
    flag = 0
    for j in range(n):
        p,c = map(int,input().strip().split())
        if p>=(x-y) and c<=k:
            print("LuckyChef")
            flag = 1
            break
    if flag==0:
        print("UnluckyChef")
