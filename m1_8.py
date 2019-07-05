from itertools import permutations
k = input()
x = list(map(int, input().split()))
r = []
for i in permutations(x, 3):
    if i[0] < i[1] < i[2]:
        if i[0] + i[1] == i[2]:
            r.append([str(j) for j in i])
for i in r:
    print(' '.join(i))
