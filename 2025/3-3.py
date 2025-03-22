import re
f = open('25-3-1.txt').read().split('\n')
print(f)

pattern = r'\d+'
ps = []
for p in range(len(f)-1):
    bxs = set()
    for j in [0,1]:
    # Find all matches in the input string
        bx = [int(i) for i in re.findall(pattern, f[p+j])]
        #print(bx)        
        for b in range(bx[0],bx[1]+1):        
            bxs.add(b)     
        for b in range(bx[2],bx[3]+1):        
            bxs.add(b)   
    print(p,bxs,len(bxs))    
    ps.append(len(bxs))  
print(max(ps))
