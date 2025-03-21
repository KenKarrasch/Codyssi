import re

f = open('25-5-1.txt').read().split('\n')

ds = []
for i in f:
    pattern = r'-?\d+'
    
    # Find all matches in the input string
    digits = re.findall(pattern, i)
    print(digits,i,abs(int(digits[0]) + int(digits[1])))
    ds.append(abs(int(digits[0])) + abs(int(digits[1])))
print(ds)
print(max(ds) - min(ds))
