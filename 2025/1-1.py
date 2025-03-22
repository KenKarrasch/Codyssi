f = open('25-1-1.txt').read().split('\n')

print(f[:-1])
cr = f[-1]
tly = int(f[0])
for pt,i in enumerate(f[1:-1]):
    print(pt,i)
    if cr[pt] == '-':
        tly -= int(i)
    else: tly += int(i)

print(tly)
