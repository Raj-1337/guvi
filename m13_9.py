from collections import Counter as c
k = input()
x = c(map(int, input().split()))
print(max(x, key=(lambda a: x[a])))
