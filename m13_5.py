from collections import Counter
x = Counter(input())
print(*list(filter((lambda a: x[a]==1), x)))
