# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X = int(input())
N = map(int,input().split())
x = int(input())
L = map(tuple,(map(int,input().split()) for _ in range(x)))
n = Counter(N)
p =0
for i in L:
    if i[0] in n.keys() and n[i[0]] >0 :
        n[i[0]] = n[i[0]]-1
        p = p+i[1]
          
print(p)
