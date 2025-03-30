f = open('25-14-1.txt').read().split('\n')

mat = []

for info in f:
    i = info.split()
    quality = int(i[5].split(',')[0])
    cost = int(i[8].split(',')[0])    
    unique = int(i[12])
    name = i[1]
    mvalue = quality/cost
    mat.append([mvalue,quality,cost,unique,name])

def select_materials(materials, budget):
    # Used Dynamic Programming
    n = len(materials)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]    
    for i in range(1, n + 1):
        cost = materials[i-1]['cost']
        quality = materials[i-1]['quality']
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-cost] + quality)
            else:
                dp[i][w] = dp[i-1][w]
    w = budget
    selected = []
    total_cost = 0    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(materials[i-1]['name'])
            w -= materials[i-1]['cost']
            total_cost += materials[i-1]['cost']
    
    return selected

materials = []

for i in mat:
    materials.append({'name': i[4], 'cost': i[2], 'quality': i[1], 'unique': i[3]})

budget = 30

result = select_materials(materials, budget)
print("Selected Materials:", result)
total_unique = 0
total_quality = 0
for i in result:
    for j in mat:
        if i == j[4]:
            total_unique += j[3]
            total_quality += j[1]
print('Total Unique:',total_unique)
print("Total Quality:", total_quality)
print(total_quality * total_unique)
