f = open('25-11-1.txt').read().split('\n')

print(f)

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
    #print(n,b)
    for i in n[::-1]:
        #print(i,getnum(i))
        num += getnum(i) * (b**place)
        #print('num',num)
        place += 1
    nums.append(num)
print(max(nums))

#abcdefghiklmnopqrstuvwxyz
#012345678901234567890123456
