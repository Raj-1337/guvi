import re
x = input()
if re.search("[a-zA-Z0-9]{3,}[&]?@gamil\.com", x):
    print("YES")
else:
    print("NO")
