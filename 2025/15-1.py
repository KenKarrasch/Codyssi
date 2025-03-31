f = open('25-15-1.txt').read().split('\n\n')

nodes = []
for i in f[0].split('\n'):
    n = i.split(' | ')
    nodes.append([n[0],int(n[1])])

sb = [nodes[0],[],[]]

def addnode(nn,lf):
    #print(lf)
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

lyr = [0]
for i in range(len(nodes)):
    lyr.append(0)
ds = []
def printnd(lf,d):    
    ds.append(d)
    for i in lf:        
        if len(i) != 2:
            printnd(i,d+1)
        else:
            sp = str(i[0]) + ' ' + str(i[1])
            for j in range(d):
                sp = '     ' + sp 
            print(sp)
            lyr[d] += i[1]


printnd(sb,0)
print(lyr)
print(max(lyr)*max(ds))
