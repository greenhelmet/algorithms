from itertools import permutations

N = int(input())
data = list(range(1, N+1))

all_permutations = list(permutations(data))

for i in all_permutations:
    print(*i)