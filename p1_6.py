
def isomorphic(s):
  a = list(set([i for i in s]))
  r = []
  for i in a:
      r.append(s.count(i))
  return r
n = input().split()
t1 = isomorphic(n[0])
t2 = isomorphic(n[1])
if sorted(t1) == sorted(t2):
  print("yes")
else:
  print("no")
