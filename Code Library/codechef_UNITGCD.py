t = int(input())
while(t):
    n = int(input())
    i = 1
    if(n==1):
        print(1)
    elif(n==0):
        print(0)
    else:
        print(n//2)
    while(n>0):
        if(n==1):
            print(1,1)
            n = n-1
            
        elif(n==3):
            print(3,i,i+1,i+2)
            n= n-3
            i = i+3
        else:
            print(2,i,i+1)
            n = n-2
            i = i+2
    t = t-1
