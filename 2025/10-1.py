f = [[int(l) for l in k.split()] for k in open('25-10-1.txt').read().split('\n')]

cols = []
rows = []
for i in range(len(f)):
    col = 0
    row = 0
    for j in range(len(f[0])):
        #print(f[i][j])
        col += int(f[i][j])
        row += int(f[j][i])
    cols.append(col)
    rows.append(row)
print(min([min(cols),min(rows)]))
