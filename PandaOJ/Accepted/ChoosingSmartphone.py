"""
INC2014A - Choosing a Smartphone
https://pandaoj.com/problem/INC2014A
Author : Daffa

INPUT

4
4
10000
5000
15000
8000
2
8000
8000
1
120000
4
8000
7000
1000
1

OUTPUT

Case #1: 64GB
Case #2: 16GB
Case #3: 128GB
Case #4: 32GB


"""

case = int(input())
count = [""]*case

for i in range(0,case):
    size = int(input())
    num = [0]*size
    for a in range(0,size):
        num[a] = int(input())
    s = sum(num)
    if(s<=16000):
        count[i] = "16GB"
    elif(s<=32000):
        count[i]  = "32GB"
    elif(s<=64000):
        count[i]  = "64GB"
    else:
        count[i]  = "128GB"
for i in range(0,case):
    j = i+1
    print("Case #"+str(j)+":",count[i])