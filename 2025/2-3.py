f = open('25-2-1.txt').read().split('\n')

print(f)
ad = int(f[0].split()[3])
ml = int(f[1].split()[3])
pw = int(f[2].split()[7])
 
ns = []
for i in f[4:]:
    ns.append(int(i))

mx = 15000000000000

tly = 0
cd = []
for i in ns:
    n = i
    n = n**pw
    n = n * ml
    n = n + ad 
    if n < mx:
        cd.append((n,i))
cd.sort()
print(cd[-1])

