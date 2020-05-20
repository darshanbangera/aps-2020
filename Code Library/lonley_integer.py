def lonelyinteger(a):
    res=0
    for i in a:
        res^=i
    return res

n = int(input())
a = list(map(int, input().strip().split()))
print(lonelyinteger(a))
