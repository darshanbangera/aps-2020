ecd = {'A':0,'B':1,'C':2,'D':3,'12':0,'3':1,'6':2,'9':3}
t = int(input())
cst = [100,75,50,25]
total = 0
for z in range(t):
    x = [[0 for c in range(4)] for v in range(4)] 
    
    n = int(input())
    for i in range(n):
        a,b = map(str,input().split())
        x[ecd[a]][ecd[b]] = x[ecd[a]][ecd[b]] + 1
    sub = 0 
    for i in range(4):
        if sum([row[i] for row in x]) == 0:
            sub = sub + 100
    m_cost = -1
    for i in range(4):
        for j in range(4):
            if(j==i):
                continue
            for k in range(4):
                if(k==i or k==j):
                    continue
                for l in range(4):
                    if(l==i or l==j or l==k):
                        continue
                    p = [x[0][i],x[1][j],x[2][k],x[3][l]]
                    
                    p.sort(reverse = True)
                    cost = 0
                    r = 100
                    for o in range(4):
                        cost = cost + (p[o]*r)
                        r = r - 25
                    if cost>m_cost:
                        m_cost = cost
                        y = [[0 for c in range(4)] for v in range(4)] 
                        y[0][i] = x[0][i]
                        y[1][j] = x[1][j]
                        y[2][k] = x[2][k]
                        y[3][l] = x[3][l]
                        sub =0
                        for q in range(4):
                            if sum(y[q])==0:
                                sub = sub +100
                        
    print(m_cost-sub)
    total = total +(m_cost-sub)
print(total)
