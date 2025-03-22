f = open('25-6-1.txt').read().split('\n')

def corrupt(j):
    if ord(j) >= ord('a'):
        if ord(j) <= ord('z'):
            return False
    if ord(j) >= ord('A'):
        if ord(j) <= ord('Z'):
            return False
    return True

def getchv(j):        
    if ord(j) >= ord('a'):
        if ord(j) <= ord('z'):
            return 1 + ord(j) - ord('a')
    if ord(j) >= ord('A'):
        if ord(j) <= ord('Z'):
            return 27 + ord(j) - ord('A')

tly = 0
for i in f:    
    ch = [getchv(i[0])]
    for c in range(1,len(i)):
        if corrupt(i[c]):      
            ch.append(((ch[-1]*2)-5)%52)
        else:            
            ch.append(getchv(i[c]))    
    for j in ch:
        tly += j    
print(tly)
