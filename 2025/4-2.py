f = open('25-4-1.txt').read().split('\n')

tly = 0


for i in f:

    l = int(len(i)/10)
    ns = ''
    for j in range(l):
        ns = ns + i[j]
    ns = ns + str(len(i) - (2*l))
    for j in range(l):
        ns = ns + i[(len(i) - l) + j]
    print('ns',ns)        
    t = 0
    for j in ns:
        if(j < 'A'):
            t += ord(j) - ord('1') + 1
        else:
            t += ord(j) - ord('A') + 1    
    print(t)
    tly += t
print(tly)
