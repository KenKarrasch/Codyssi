import re
f = open('25-3-1t.txt').read().split('\n')
print(f)

pattern = r'\d+'

tly = 0
for q in f:
    # Find all matches in the input string
    bx = [int(i) for i in re.findall(pattern, q)]
    print(bx)
    bxs = set()
    for b in range(bx[0],bx[1]+1):        
        bxs.add(b)     
    for b in range(bx[2],bx[3]+1):        
        bxs.add(b)         
    tly += len(bxs)   

print(tly)
