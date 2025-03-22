f = open('25-6-1.txt').read().split('\n')

ct = 0
for i in f:    
    for j in i:
        if ord(j) >= ord('a'):
            if ord(j) <= ord('z'):
                ct += 1 + ord(j) - ord('a')
        if ord(j) >= ord('A'):
            if ord(j) <= ord('Z'):
                ct += 27 + ord(j) - ord('A')
print(ct)
