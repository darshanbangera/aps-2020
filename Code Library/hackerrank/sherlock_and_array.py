for t in range(int(input())):
    n = int(input())
    arr = [int(b) for b in input().split()]
    sm = sum(arr)
    c = 0
    for i in range(n):
        if 2*c == sm-arr[i]:
            print("YES")
            break
        c =c+ arr[i]
    else:
        print("NO")
