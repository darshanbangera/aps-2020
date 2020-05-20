t = int(input())
for z in range(t):
    n,p = map(int, input().split())
    d =list(map(int,input().split()))
    vals = {}
    div = [0]*n
    flag = 0
    for i in range(n):
        if i==n-1:
            if(p%d[n-1]!=0):
                flag=1
        else:
            for j in range(i+1,n):
                if((d[j]%d[i] != 0) or (p % d[i] != 0)):
                    flag = 1
    if(flag == 0):
        print("NO")
        continue
    else:
        for i in range(n-1,-1,-1):
            if((p % d[i]) == 0):
                div[i] = (p // d[i]) - 1
                p = p - (div[i] * d[i])
            else:
                div[i] = (p // d[i]) + 1;
                break;
    print("YES",end=' ')
    for i in div:
        print(i,end=' ')
    print()
