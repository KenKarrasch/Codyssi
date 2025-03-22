import re
f = open('25-3-1.txt').read().split('\n')
print(f)

pattern = r'\d+'

tly = 0
for i in f:
    # Find all matches in the input string
    bx = [int(i) for i in re.findall(pattern, i)]
    print(bx)
    tly += 1 + bx[1] - bx[0]
    tly += 1 + bx[3] - bx[2]
print(tly)
