t = int(input())
for i in range(t):
    n,c = map(int,input().split()) 
    a = list(map(int,input().split()))
    sum=0
    for j in range(n):
        sum = sum+a[j]
    if sum <= c:
        print("Yes")
    else:
        print("No")
