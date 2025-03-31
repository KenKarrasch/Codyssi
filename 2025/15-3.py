f = open('25-15-1.txt').read().split('\n\n')

nodes = []
for i in f[0].split('\n'):
    n = i.split(' | ')
    nodes.append([n[0],int(n[1])])

anc = []
for i in f[1].split('\n'):
    n = i.split(' | ')
    anc.append([n[0],int(n[1])])

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
addnode(anc[0],sb)

seq = ''
for i in sq:
    seq = seq + '-' + i

sq = []
addnode(anc[1],sb)

nseq = ''
for i in sq:
    nseq = nseq + '-' + i


cm = []

done = False
i = 1
while not done:    
    if i >= len(seq) or i >= len(nseq):
        done = True
    if seq[i] == nseq[i]:
        cm.append(seq[i])
    else:
        done = True
    i += 1    

cm = cm[0:-1]
ncm = []
for i in cm[::-1]:
    if i == '-':
        break
    ncm.append(i)

nncm = ''
for i in ncm[::-1]:
    nncm = nncm + i
print(nncm)
