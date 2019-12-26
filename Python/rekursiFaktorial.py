# Function factorial rekursif

def fac(num):
    global ulang
    ulang+=1
    if(num == 1):
        print('1')
        return 1
    print(num,'* ',end='')
    return num*fac(num-1)

# Main

ulang = 0
num = int(input('Faktorial dari : '))
print()
print('Faktorial dari',num,':',fac(num))
print('Pemanggilan function di lakukan sebanyak :', ulang)
print()

