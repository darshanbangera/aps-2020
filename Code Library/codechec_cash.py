t = int(input())
for z in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    rems = []
    needed = []
    for c in range(n):
        rems.append(arr[c]%k)
        needed.append(k-rems[c])
    for c in range(0,n):
        val = 0
        val = (sum(rems[:c]) - sum(needed[c:]))%k
        if(c == 0):
            min_leftover = val
        elif(val<min_leftover):
            min_leftover = val
    print(min_leftover)
