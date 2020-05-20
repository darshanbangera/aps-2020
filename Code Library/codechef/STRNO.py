t = int(input())
while(t):
    t = t -1
    x , K = map(int,input().split())
    arr = []
    while(x%2 == 0):
        arr.append(2)
        x = x/2
    i = 3
    while (i * i <= x): 
        while (x % i == 0) :
            x = x/i
            arr.append(2)
        i =i + 2
    if (x > 2):
        arr.append(x)
    if(len(arr) >= K):
        print(1) 
    else:
        print(0)
