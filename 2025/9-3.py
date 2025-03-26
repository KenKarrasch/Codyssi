f = open('25-9-1.txt').read().split('\n\n')

wlt = {}
debts = []

def settledebts():
    for dt in range(len(debts)):        
        if wlt[debts[dt][0]] > 0:            
            amt = min(wlt[debts[dt][0]],debts[dt][2])
            if wlt[debts[dt][0]] > debts[dt][2]:
                print('has enough to pay debt')
            else:
                print('not enough to pay debt')
            print('settling debt',amt)
            wlt[debts[dt][1]] += amt
            wlt[debts[dt][0]] -= amt
            debts[dt][2] -= amt            
            print('wallet',wlt)
            print('debts',debts)
    ndebts = []
    for i in debts:
        if i[2] != 0:
            ndebts.append(i[:])
    debts.clear()    
    for i in ndebts:
        debts.append(i[:])

for i in f[0].split('\n'):
    w = i.split()    
    wlt[w[0]] = int(w[2])
for i in f[1].split('\n'):
    t = i.split()    
    print(i)
    amt = int(t[5])
    if amt > wlt[t[1]]:
        debts.append([t[1],t[3],amt - wlt[t[1]]])
        amt = wlt[t[1]]            
    wlt[t[1]] -= amt
    wlt[t[3]] += amt    
    print('wallet',wlt)
    print('debts',debts)
    settledebts()
    print('-----------------')

v = list(wlt.values())
print(wlt)
print('======')
for i in debts:
    print(i)
v.sort()
print(v)
print(len(debts))
print(sum(v[-3:]))

