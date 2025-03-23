f = open('25-7-1.txt').read().split('\n\n')
fs = []
for i in f[0].split('\n'):
    fs.append(i)
sp = []
for i in f[1].split('\n'):
    st = int(i.split('-')[0])
    ed = int(i.split('-')[1])
    sp.append((st,ed))
for i in sp:
    print(i)
    fst = fs[i[0]-1]
    fs[i[0]-1] = fs[i[1]-1]
    fs[i[1]-1] = fst
print(fs[int(f[2])-1])
