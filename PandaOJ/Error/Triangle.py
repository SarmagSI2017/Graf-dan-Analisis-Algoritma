"""
Triangle
https://pandaoj.com/problem/JC3A
Author : Daffa
Memory Limit Exceeded

INPUT
2
3
10

OUTPUT
Case #1: 1
Case #2: 6

"""

case = int(input())
count = []
for i in range(0,case):
    length = int(input())
    count.append(0)
    for a in range(1,length-1):
        for b in range(length-(a+1),0,-1):
            c = length-(a+b)
            num = [a,b,c]
            num.sort()
            if(num[0]+num[1])>num[2]:
                count[i] += 1

for i in range(0,case):
    j = i +1
    print("Case #"+str(j)+":",count[i])