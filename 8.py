import re

s = str(input())

print(re.findall("[a-zA-Z][a-z]*", s))