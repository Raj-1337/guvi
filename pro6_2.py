x, y = 0, 0
for _ in range(4):
    u, v = map(int, input().split())
    x += u
    y += v
print('yes') if x == y else print('no')
