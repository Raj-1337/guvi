from itertools import combination_with_replacement
n = int(input())
c = 0
t = (n // 2) + 1
for j in range(1, t):
    for i in combination_with_replacement([1,2], j):
        if sum(i) == n: c += 1
print(c)
