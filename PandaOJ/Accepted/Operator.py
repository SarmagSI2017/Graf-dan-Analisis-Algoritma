"""
OPERATOR
https://pandaoj.com/submission/78884
Author : Daffa

INPUT
5
1 2 3
3 1 2
2 2 4
2 4 8
3 7 0

OUTPUT
Kasus #1: +
Kasus #2: -
Kasus #3: +
Kasus #4: *
Kasus #5: TIDAK ADA SOLUSI

"""

case = int(input())
op = []

for i in range(0,case):
    raw = input()
    a = raw.split()
    if int(a[0])+int(a[1]) == int(a[2]):
        op.append('+')
    elif int(a[0])-int(a[1]) == int(a[2]):
        op.append('-')
    elif int(a[0])*int(a[1]) == int(a[2]):
        op.append('*')
    elif int(a[0])/int(a[1]) == int(a[2]):
        op.append('/')
    else:
        op.append("TIDAK ADA SOLUSI")

for i in range(0,case):
    print("Kasus #"+str(i+1)+":",op[i])