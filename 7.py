import re

s = str(input())
s = s + "_"
t = re.findall("[a-z]+_", s)
for i in range(len(t)):
    t[i] = t[i].capitalize()
u = ''.join(t)
v = re.sub("_", "", u)
print(v)