f = open('25-8-1.txt').read().split('\n')

print(f)

lc = 0
tly = 0

for i in f:
    chc = []
    for j in range(len(i)):
        chc.append(i[j])
    print(chc)
    j = 0
    nums = True
    while nums:
        lght = len(chc)
        j = 0
        while j < len(chc)-1:        
            #print(chc[j],chc[j+1],j)
            #print('j',j)
            if chc[j].isdigit():
                if not chc[j+1].isdigit():                    
                    if chc[j] != '-' and chc[j+1] != '-':
                        chc = chc[:j] + chc[j+2:]                
                        #print(chc)                  
            j += 1

        j = 0
        while j < len(chc)-1:        
            #print(chc[j],chc[j+1],j)
            #print('j',j)
            if not chc[j].isdigit():
                if chc[j+1].isdigit():
                    if chc[j] != '-' and chc[j+1] != '-':
                        chc = chc[:j] + chc[j+2:]                
                        #print(chc)                  
            j += 1

        nums = True
        print(chc)
        if lght == len(chc):
            nums = False
    tly += len(chc)
print(tly)
    

