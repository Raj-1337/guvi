from collections import Counter
l = input()
n = Counter(input())
maxx = min(n.keys(), key=(lambda x: n[x]))
print(maxx)
