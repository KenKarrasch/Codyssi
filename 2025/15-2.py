f = open('25-15-1.txt').read().split('\n\n')

nodes = []
for i in f[0].split('\n'):
    n = i.split(' | ')
    nodes.append([n[0],int(n[1])])

sb = [nodes[0],[],[]]

sq = []

def addnode(nn,lf):    
    sq.append(lf[0][0])
    if lf[0][1] > nn[1]:
        if lf[1] == []:
            lf[1] = [nn,[],[]]
        else:
            addnode(nn,lf[1])
    if lf[0][1] < nn[1]:
        if lf[2] == []:
            lf[2] = [nn,[],[]]
        else:
            addnode(nn,lf[2])         

for n in nodes:
    addnode(n,sb)
sq = []
addnode(['end',500000],sb)
print(sq)
seq = ''
for i in sq:
    seq = seq + '-' + i
print(seq)

