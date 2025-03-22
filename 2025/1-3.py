f = open('25-1-1.txt').read().split('\n')
cr = f[-1][::-1]
tly = int(f[0])*10 + int(f[1])

ns = []
for i in range(int(len(f[1:-1])/2)):
    print(int(f[2*i+2]),int(f[2*i+3]))
    ns.append(int(f[2*i+2])*10 + int(f[2*i+3]))

for pt,i in enumerate(ns):
    print(pt,i)
    if cr[pt] == '-':
        tly -= int(i)
    else: tly += int(i)

print(tly)
