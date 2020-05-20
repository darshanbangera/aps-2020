from sys import stdin,stdout

def c(n):
    n=int(n)
    if bin(n).count("1")&1:
        return 1
    return 0

t=int(input())
for _ in range(t):
    x=list(map(int,input().split()))
    li=list(map(c,stdin.readline().split()))
    su=sum(li)
    zq=(x[0]-su,su)
    oq=zq[::-1]
    for _ in range(x[1]):
        q=int(stdin.readline())
        if bin(q).count("1")&1:#even no of 1s
            print(*oq)
        else:#odd
            print(*zq)
