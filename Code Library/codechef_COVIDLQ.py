# cook your dish here
t = int(input())
while(t):
    n = int(input())
    arr = list(map(int,input().split()))
    count = 0
    flag = 0
    check = 0 
    for i in range(n):
        if(flag == 0 and arr[i]==1):
            count = 0
            flag = 1 
        elif(flag == 1 and arr[i]==0):
            count = count + 1
        elif(flag==1 and arr[i]==1):
            if(count>=5):
                count = 0
            elif(count<5):
                check =1 
            count = 0
        if(check == 1):
            break
    if(check==1):
        print("NO")
    else:
        print("YES")
    t = t-1
    
