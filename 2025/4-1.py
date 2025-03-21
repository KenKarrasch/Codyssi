f = open('25-4-1.txt').read().split('\n')

tly = 0

for i in f:
    for j in i:
        tly += ord(j) - ord('A') + 1
print(tly)
