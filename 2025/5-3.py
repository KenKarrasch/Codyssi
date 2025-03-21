import re

f = open('25-5-1.txt').read().split('\n')

def gdig(st):
    pattern = r'-?\d+'
    return([int(i) for i in re.findall(pattern, st)])

nr = [0,0]
ds = []
for i in f:
    d = gdig(i)    
    ds.append((d[0], d[1]))
tly = 0
for i in range(len(f)):    
    nds = []
    for d in ds:            
        nds.append((abs(d[0]-nr[0]) + abs(d[1]-nr[1]), d[0], d[1]))
    nds.sort()    
    print(nds[0])
    d = [nds[0][1],nds[0][2]]
    tly += abs(d[0]-nr[0]) + abs(d[1]-nr[1])
    nr = [nds[0][1],nds[0][2]]    
    nnds = []
    for n in nds[1:]:
        nnds.append((n[1],n[2]))
    ds = []    
    for n in nnds:
        ds.append((n[0],n[1]))    
print(tly)
