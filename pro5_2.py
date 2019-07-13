n, k = map(int, input().split())
x = list(map(int, input().split()))
r = []
for i in range(0, len(x)+1, k):
    if i+k > len(x):
        break
    r.append(min(x[i:i+k]))
print(max(r))
