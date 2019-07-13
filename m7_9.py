import re
x = input()
if re.search("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+", x):
    print("YES")
else:
    print("NO")
