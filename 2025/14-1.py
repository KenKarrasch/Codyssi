f = open('25-14-1.txt').read().split('\n')

print(f)

mat = []

for info in f:
    i = info.split()
    quality = int(i[5].split(',')[0])
    cost = int(i[8].split(',')[0])
    print(i[12])
    unique = int(i[12])
    name = i[1]
    mat.append([quality,cost,unique,name])

mat.sort()
print(mat)

print(mat[-1][2] + mat[-2][2] + mat[-3][2] + mat[-4][2] + mat[-5][2])
