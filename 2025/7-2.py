f = open('25-7-1.txt').read().split('\n\n')
fs = []
for i in f[0].split('\n'):
    fs.append(i)
sp = []
sr = f[1].split('\n')
for i in range(len(sr)):
    st = int(sr[i].split('-')[0])
    ed = int(sr[i].split('-')[1])
    if i == len(sr)-1:
        ed2 = int(sr[0].split('-')[0])
    else:
        ed2 = int(sr[i+1].split('-')[0])
    sp.append((st,ed,ed2))
for i in sp:
    print(i)
    fst1 = fs[i[0]-1]
    fst2 = fs[i[1]-1]
    fst3 = fs[i[2]-1]
    fs[i[0]-1] = fst3
    fs[i[1]-1] = fst1
    fs[i[2]-1] = fst2
print(fs[int(f[2])-1])
