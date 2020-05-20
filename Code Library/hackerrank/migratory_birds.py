import sys
from collections import Counter

n = int(input().strip())
types = list(map(int, input().strip().split(' ')))

p = Counter(types)

m = max(p.values())
f = [k for k,v in p.items() if v == m]
print(min(f))
