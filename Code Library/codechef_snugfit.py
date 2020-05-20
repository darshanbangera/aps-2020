for cases in range(int(input())):
    n = int(input())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    arr1.sort()
    arr2.sort()
    dia_sum = 0
    for i in range(n):
        dia_sum = dia_sum + min(arr1[i],arr2[i])
    print(dia_sum)
