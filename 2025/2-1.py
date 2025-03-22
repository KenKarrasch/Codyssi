f = open('25-2-1.txt').read().split('\n')

print(f)
ad = int(f[0].split()[3])
ml = int(f[1].split()[3])
pw = int(f[2].split()[7])
 
ns = []
for i in f[4:]:
    ns.append(int(i))

ns.sort()
print(ns)
med = ns[int(len(ns)/2)]

print(med)
for i in [med]:
    n = int(i)
    n = n**pw
    n = n * ml
    n = n + ad 
print(n)

