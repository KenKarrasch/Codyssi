f = open('25-9-1.txt').read().split('\n\n')

print(f)
wlt = {}
for i in f[0].split('\n'):
    w = i.split()    
    wlt[w[0]] = int(w[2])

for i in f[1].split('\n'):
    t = i.split()    
    amt = int(t[5])
    if amt > wlt[t[1]]:
        amt = wlt[t[1]]    
    wlt[t[1]] -= amt
    wlt[t[3]] += amt
    print(wlt)
v = list(wlt.values())
v.sort()
print(sum(v[-3:]))

