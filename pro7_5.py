n, k = map(int, input().split())
x = list(map(int, input().split()))
a = int(input())
c = (sum(x)-x[k]) / 2
print('Bon Appetit') if a == c else print(int(a-c))
