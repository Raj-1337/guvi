from itertools import combinations
n, k, t = map(int, input().split())
x = list(map(int ,input().split()))
for i in combinations(x, k):
    if sum(i) == t:
        print('YES')
        break
else:
    print('NO')
