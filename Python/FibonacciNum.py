# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# 1, 2, 3, 4, 5, 6, 7, 8 ,  9, 10, 11, 12,  13, ....

# Print Urutan Fibbonaci
def fibprint(urutan):
    con = [0,1]
    for i in range(2,urutan):
        con.append(con[i-1]+con[i-2])
    print(con)

def fib(urutan):
    global ulang
    ulang+=1
    if(urutan == 1):
        return 0
    elif(urutan <= 2):
        return 1
    else:
        return fib(urutan-1)+fib(urutan-2)

ulang = 0
n = int(input('urutan : '))
print()
fibprint(n)
print()
print('Fibbonaci Sequence pada urutan',n,':',fib(n))
print('Pemanggilan function di lakukan sebanyak :', ulang)
print()