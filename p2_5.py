
from collections import Counter
n = Counter(input())
maxx = max(n.keys(), key=(lambda x: n[x]))
print(maxx)
