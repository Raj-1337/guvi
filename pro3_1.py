from statistics import mean
from itertools import permutations
k = int(input())
x = list(map(int, input().split()))
flag = True
for i in permutations(x, len(x)):
    if flag:
        for j in range(1, len(i)):
            t1 = i[:j]
            t2 = i[j:]
            print("loop:", t1, t2)
            a1 = mean(t1)
            a2 = mean(t2)
            print("avg:", a1, a2)
            if a1 == a2:
                print('yes')
                flag = False
                break
    else:
        break
    print("\n")
else:
    print('no')
