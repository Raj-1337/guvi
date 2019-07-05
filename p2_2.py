
n = list(map(int, input().split()))
k = n[-1]
ar = [int(i) for i in input().split()]
for _ in range(k):
  ar.insert(0, ar.pop())
for i in ar:
  print(i, end=" ")
