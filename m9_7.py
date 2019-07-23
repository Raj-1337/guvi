n, k = map(int, input().split())
x = [i for i in list(map(int, input().split())) if i <= k]
print(len(x))
