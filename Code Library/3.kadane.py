x = int(input())
arr = list(map(int,input().split()))
def find_max(a):
    max_current = a[0]
    max_global = a[0]
    start= 0 
    end= 0
    s=0
    for i in range(1,len(a)):
        max_current = max(a[i],max_current+a[i])
        if(max_current == a[i]):
            s = i
        if max_current > max_global:
            max_global = max_current
            start = s
            end = i
    return start,end,max_global

s,e,m1_val = find_max(arr)
print(m1_val)
