t = int(input())
while(t):
    n = int(input())
    arr = list(map(int,input().split()))
    profit = 0
    arr.sort(reverse = True)
    for i in range(n):
        if(arr[i]-i>0):
            arr[i] = arr[i] - i
        else:
            arr[i] = 0
        profit = profit + arr[i]
    print(profit % 1000000007)
    t = t - 1
