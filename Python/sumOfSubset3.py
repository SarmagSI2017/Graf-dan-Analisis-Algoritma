item = [1,2,3]
search = 2

subset = []
solveSub = []

for a in range(0,len(item)):
    for b in range(0,len(item)):
        for c in range(0,len(item)):
            sub = [item[a],item[b],item[c]]
            if(sum(sub) == search):
                solveSub.append(sub)
            subset.append(sub)

print(subset)
print(solveSub)