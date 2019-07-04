
n = int(input())
flag = False
for i in range(1, n+1):
  if n % i == 0:
    break
if not flag:
  print("yes")
else:
  print("no")
    
