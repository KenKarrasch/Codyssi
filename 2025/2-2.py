f = open('25-2-1.txt').read().split('\n')

print(f)
ad = int(f[0].split()[3])
ml = int(f[1].split()[3])
pw = int(f[2].split()[7])
 
ns = []
for i in f[4:]:
    ns.append(int(i))

tly = 0
for i in ns:
    if i % 2 == 0:
        print(i)
        tly += i
n = tly
n = n**pw
n = n * ml
n = n + ad 
print(n)

