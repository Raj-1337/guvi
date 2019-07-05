from itertools import permutations
n, k = map(int, input().split())
x = list(map(int, input().split()))
for i in permutations(x, 2):
    if sum(i) == k:
        print('YES')
        break
else:
    print('NO')
