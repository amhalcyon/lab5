import re

s = str(input())
t = re.findall('[A-Z][a-z]*', s)
u = ' '.join((t))
u = u.lower()

print(re.sub("\s", "_", u))