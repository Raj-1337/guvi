n = int(input())
r = []
for i in range(pow(2, n)):
    r.append(bin(i)[2:].zfill(n))
r.sort(key=(lambda x: x.count('1')))
for i in r:
    print(i)
