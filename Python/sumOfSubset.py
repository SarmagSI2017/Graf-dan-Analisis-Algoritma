from itertools import combinations
 
def solve(items,search):
    global ulang
    solve_subset = []
    print(items)
    for length in range(1, len(items)):
        for subset in combinations(items, length):
            ulang+=1
            print(subset, end='')
            if(sum(subset) == search):
                solve_subset.append(subset);
        print()
    print({})

ulang = 2


items = {1,2,3}
search = 2

solve(items,search)
print('perulangan :',ulang)
print()
#ulang = 2
#solve({5,10,12,13,15,18})
#print('perulangan :',ulang)