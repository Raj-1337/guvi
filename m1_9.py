from itertools import permutations
k = input()
x = list(map(int, input().split()))
r = 0
c = 10000
for i in permutations(x, 2):
    if sum(i) == 0:
        r = i
        break
    elif 0-sum(i) < c:
        c = 0-sum(i)
        r = i
print(r[0], r[1])
