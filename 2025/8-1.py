f = open('25-8-1.txt').read().split('\n')

print(f)

lc = 0
for i in f:
    for j in i:
        if ord(j) >= ord('a'):
            if ord(j) <= ord('z'):
                lc += 1
        if ord(j) >= ord('A'):
            if ord(j) <= ord('Z'):
                lc += 1
print(lc)
