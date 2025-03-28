f = open('25-12-1.txt').read().split('\n\n')

#print(f)
gd = []

for g in f[0].split('\n'):
    ln = []
    for i in g.split():
        ln.append(int(i))
    gd.append(ln)

def prtgd():
    for i in gd:
        print(i)
    print()

prtgd()
L = len(gd[0])
H = len(gd)
print(L,H)
insts = [i.split() for i in f[1].split('\n')]
#print(insts)



def act(taken):
    i = 0
    if taken[0] == 'SHIFT':
        rl = int(taken[2])-1
        nl = []
        if taken[1] == 'ROW':
            for itm in range(L):
                nl.append(gd[rl][(itm - int(taken[4]))%L])            
            for itm in range(L):
                gd[rl][itm] = nl[itm]
        if taken[1] == 'COL':
            for itm in range(H):
                nl.append(gd[(itm - int(taken[4]))%H][rl])
            for itm in range(H):
                gd[itm][rl] = nl[itm]
    if taken[0] == 'MULTIPLY':                
        if taken[2] == 'ROW':
            rl = int(taken[3])-1
            for itm in range(L):
                gd[rl][itm] = (int(taken[1]) * gd[rl][itm]) % 1073741824
        if taken[2] == 'COL':
            rl = int(taken[3])-1
            for itm in range(H):
                gd[itm][rl] = (int(taken[1]) * gd[itm][rl]) % 1073741824
        if taken[2] == 'ALL':
            for itml in range(L): 
                for itmh in range(H):
                    gd[itml][itmh] = (int(taken[1]) * gd[itml][itmh]) % 1073741824
    if taken[0] == 'ADD':                
        if taken[2] == 'ROW':
            rl = int(taken[3])-1
            for itm in range(L):
                gd[rl][itm] = (int(taken[1]) + gd[rl][itm]) % 1073741824 
        if taken[2] == 'COL':
            rl = int(taken[3])-1
            for itm in range(H):
                gd[itm][rl] = (int(taken[1]) + gd[itm][rl]) % 1073741824   
        if taken[2] == 'ALL':
            for itml in range(L): 
                for itmh in range(H):
                    gd[itml][itmh] = (int(taken[1]) + gd[itml][itmh]) % 1073741824            
    if taken[0] == 'SUB':
        if taken[2] == 'ROW':
            rl = int(taken[3])-1
            for itm in range(L):
                gd[rl][itm] = (gd[rl][itm] - int(taken[1])) % 1073741824
        if taken[2] == 'COL':
            rl = int(taken[3])-1
            for itm in range(H):
                gd[itm][rl] = (gd[itm][rl] - int(taken[1])) % 1073741824      
        if taken[2] == 'ALL':
            for itml in range(L): 
                for itmh in range(H):
                    gd[itml][itmh] = (gd[itml][itmh] - int(taken[1])) % 1073741824
    prtgd()


fc = f[2].split('\n')
stg = []
for i in fc:    
    print(i)
    if i == 'TAKE':        
        stg = insts[0][:]
        print('stg',stg)
        insts = insts[1:] 
    if i == 'CYCLE':        
        insts.append(stg)
    if i == 'ACT':        
        act(stg)    
        stg = [] 
    for isnt in insts:
        print(isnt)
    prtgd()

rs = []
for i in gd:
    rs.append(sum(i))
    
for i in range(L):
    sm = 0
    for j in range(L):
        sm += gd[j][i]
    rs.append(sm)

print(rs)
print(max(rs))

