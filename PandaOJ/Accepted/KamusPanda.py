"""
Kamus Panda
https://pandaoj.com/problem/BNPCHS2008A
Author : Daffa

INPUT
3
lalala
panda
acm

OUTPUT
2
4
3

"""

case = int(input())
count = [0]*case
for i in range(0,case):
    string = input()
    count[i] = len(''.join(set(string)))

for i in range(0,case):
    print(count[i])