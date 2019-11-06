"""
JOLLYREC17QUALP - Faktorial
https://pandaoj.com/problem/JOLLYREC17QUALP
Author : Daffa

Carilah nilai n maksimum sehingga 25! > 3n

"""

def fact(n):
    fact = 1

    for i in range(1,n+1): 
        fact = fact * i 
    return fact

const = fact(25)
for i in range(0,100):
    if not(const>pow(3,i)) :
        print(i-1)
        break
