f = open('25-11-1.txt').read().split('\n')

#print(f)

def getnum(ch):
    if ord('0') <= ord(ch) <= ord('9'):
        return(ord(ch) - ord('0'))
    if ord('A') <= ord(ch) <= ord('Z'):
        return(10 + ord(ch) - ord('A'))
    if ord('a') <= ord(ch) <= ord('z'):
        return(36 + ord(ch) - ord('a'))

nums = []

for nb in f:
    n,b = nb.split()
    b = int(b)
    n = [i for i in n]
    num = 0
    place = 0    
    for i in n[::-1]:        
        num += getnum(i) * (b**place)        
        place += 1
    nums.append(num)
print(sum(nums))

amt = sum(nums)
bi = 1
while True:
    n = '10000'
    b = int(bi)
    n = [i for i in n]
    num = 0
    place = 0    
    for i in n[::-1]:        
        num += getnum(i) * (b**place)        
        place += 1    
    print(num,b)
    if num > amt:        
        print(amt,num,b)
        break
    bi += 1



