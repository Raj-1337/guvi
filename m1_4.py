from collections import Counter
k = input()
x = list(map(int, input().split()))
t = Counter(x)
print(min(t.keys(), key=(lambda x: t[x])))
