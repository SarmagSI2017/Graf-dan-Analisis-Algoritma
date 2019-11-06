"""
Maximum Matrix Cover
https://pandaoj.com/problem/IDEAFUSE16J
Author : Daffa

INPUT
5
2 1
5 -10
-10 7
2 1
5 -1
-1 7
2 2
5 -1
-1 7
3 2
-1 2 3
4 -5 6
7 8 -9
3 2
1 -2 -3
-4 5 -6
-7 -8 9


OUTPUT
Case #1: 7
Case #2: 10
Case #3: 12
Case #4: -1
Case #5: 14


"""

import numpy as np

def summat(matrix):
    sam = 0
    for i in range(0,len(matrix)):
        for j in range(0, len(matrix)):
            sam += matrix[i][j]
    return sam

case = int(input())

caseout = []

for a in range(0,case):
    rs = input()
    rs = rs.split()
    r = int(rs[0])
    s = int(rs[1])
    raw = ""
    for i in range(0,r):
        raw += input()
        raw += " "
    entries = list(map(int, raw.split())) 

    # For printing the matrix 
    matrix = np.array(entries).reshape(r, r)
    #print(matrix)

    sub = 1
    allsubm = []

    for i in range(0,r):
        subm = []
        print("--")
        if(i==r-1):
            subm.append(matrix[0][0])
        subm.append(matrix[i][i])
        sub += 1
        if(sub > s):
            break
        for j in range(i+1,r):
            subm.append(matrix[j][j])
            sub +=1
            if(sub > s):
                break
        print(subm)
        allsubm.append(sum(subm))
    print("semua    : ",allsubm)
    print("terbesar : ",max(allsubm))


    