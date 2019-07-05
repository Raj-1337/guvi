k = input()
x = list(map(int, input().split()))
x.sort(reverse=True)
y = [str(i) for i in x]
print("->".join(y))
