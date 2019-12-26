items = [1,2,3]
#items = [5,10,12,13,15,18]
print(items)

col_subsets = []

for length in range(1,len(items)):
    for a in range(len(items)):
        c = a
        subset = []

        for b in range(length):
            if(c == 0):
                subset.append(items[c])
            elif(c < len(items)):
                subset.append(items[c])
            elif c == len(items):
                subset.append(items[0])
            if(c < len(items)):
                c+=1
        print(subset,end='')
        print('sum : ',sum(subset))
        col_subsets.append(subset)
    #print()
print({})
print('banyak subset : ',len(col_subsets)+2)