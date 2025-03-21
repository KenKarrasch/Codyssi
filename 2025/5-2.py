import re

f = open('25-5-1.txt').read().split('\n')

def gdig(st):
    pattern = r'-?\d+'
    return([int(i) for i in re.findall(pattern, st)])

ds = []
for i in f:    
    digits = gdig(i)
    print('digits',digits)
    print(digits,i,abs(digits[0]) + abs(digits[1]))
    ds.append([abs(digits[0]) + abs(digits[1]),i])

ds.sort()
print(ds)
print(ds[0][1])
nr = [int(i) for i in gdig(ds[0][1])]
print('nr',nr)
nds = []
for i in f:
    digits = gdig(i)
    print(digits)
    nds.append([abs(digits[0]-nr[0]) + abs(digits[1]-nr[1]),i])
nds.sort()
print(nds)
print(nds[1])
