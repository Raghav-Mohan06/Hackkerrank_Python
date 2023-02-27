from itertools import permutations

S = input().split()

for i in sorted(permutations(S[0], int(S[1]))):
    print(''.join(i))
