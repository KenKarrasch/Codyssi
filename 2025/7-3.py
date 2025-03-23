f = open('25-7-1.txt').read().split('\n\n')
fs = []
for i in f[0].split('\n'):
    fs.append(i)
sp = []
for i in f[1].split('\n'):
    st = int(i.split('-')[0])
    ed = int(i.split('-')[1])
    sp.append((st,ed))
for q in sp:
    print(q)
    snp1,snp2 = [],[]
    i = [min(q),max(q)]
    lgte = 1 + len(fs) - i[1]
    lgtb = i[1] - i[0]
    pl = min(lgte,lgtb)    
    for j in range(pl):
        snp1.append(fs[i[0]+j-1])    
    for j in range(pl):
        snp2.append(fs[i[1]+j-1])    
    for j in range(pl):
        fs[i[1]+j-1] = snp1[j]
    for j in range(pl):
        fs[i[0]+j-1] = snp2[j]   
print(fs[int(f[2])-1])
