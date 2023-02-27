from itertools import product

A = input().split()
A = list(map(int, A))
B = input().split()
B = list(map(int, B))

for i in product(A, B):
    print (i,end=" ")
