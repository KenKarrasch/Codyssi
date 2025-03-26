f = open('25-9-1.txt').read().split('\n\n')

print(f)
wlt = {}
for i in f[0].split('\n'):
    w = i.split()    
    wlt[w[0]] = int(w[2])

for i in f[1].split('\n'):
    t = i.split()    
    wlt[t[1]] -= int(t[5])
    wlt[t[3]] += int(t[5])
    print(wlt)
v = list(wlt.values())
v.sort()
print(sum(v[-3:]))

