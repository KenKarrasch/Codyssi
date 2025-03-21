f = open('25-4-1.txt').read().split('\n')

tly = 0
for i in f:
    cl = i[0]
    ns = i[0]
    rl = 0
    for j in i:
        if cl == j:
            rl += 1
        else:            
            ns = ns + str(rl) + j
            rl = 1
            cl = j
    ns = ns + str(rl)
    print(ns)
    t = 0
    for j in ns:
        if(j < 'A'):
            t += ord(j) - ord('1') + 1
        else:
            t += ord(j) - ord('A') + 1    
    print(t)
    tly += t
print(tly)
