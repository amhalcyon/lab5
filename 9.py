import re

s = str(input())
t = re.findall('[A-Z][a-z]*', s)

print(' '.join((t)))