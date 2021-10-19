#grupa B

from random import *

'''#wzór Z1
a = 4.25
b = 3
w = (a*b**2) / (3 * a**0.5)
print(w)

#najmniejsza Z2
a = float(input())
b = float(input())
c = float(input())
if a<b:
    if a<c:
        print(a)
    else:
        if b<c:
            print(b)
        else:
            print(c)
else:
    if b<c:
        print(b)
    else:
        print(c)

#pole wzorem herona Z3
a = float(input())
b = float(input())
c = float(input())
p = (a+b+c)/2
area = (p*(p-a)*(p-b)*(p-c))**0.5
print(area)

#iloczyn Z4
i = 1
n=float(input())
if n>40:
    i = 0
while n<=40:
    i*=n
    n=float(input())
print(i)

#wypisanie ciągu Z5
a0 = -3
for i in range(5):
    print(a0 * 2**i * (-1)**i)

#suma Z6
a0 = -10
s=0
n = int(input())
for i in range(n):
   s += a0 + 6*i
print(s)'''

#ułamki Z7
def lowest_possible_denominaor(num, den):
    if num>den:
        buff1 = num
        buff2 = den
    else:
        buff2 = num
        buff1 = den
    while(buff2!=0):
        buff3 = buff2
        buff2 = buff1%buff2
        buff1 = buff3
    if buff1 != 1:
        num = num/buff1
        den = den/buff1
    whole = num//den
    if num > den/2:
        if whole<0:
            whole += 1
        else:
            whole -= 1
    return [num, den, whole]

def addition(a, b, c, d):
    numerator = a*d + b*c
    denominator = b*d
    return lowest_possible_denominaor(numerator, denominator)

def subtraction(a, b, c, d):
    numerator = a*d - b*c
    denominator = b*d
    return lowest_possible_denominaor(numerator, denominator)

def multiplication(a, b, c, d):
    numerator = a*c
    denominator = b*d
    return lowest_possible_denominaor(numerator, denominator)

def division(a, b, c, d):
    numerator = a*d
    denominator = b*c
    return lowest_possible_denominaor(numerator, denominator)
print("enter fractions: a/b and c/d")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if b==0 or d==0:
    print("critical error, division by 0")
else:
    add = addition(a,b,c,d)
    sub = subtraction(a,b,c,d)
    mul = multiplication(a,b,c,d)
    div = division(a,b,c,d)
    print(add[2], " and ", add[0], '/', add[1])
    print(sub[2], " and ", sub[0], '/', sub[1])
    print(mul[2], " and ", mul[0], '/', mul[1])
    print(div[2], " and ", div[0], '/', div[1])


#schemat blokowy
ile = 0
i = 1
while i<=100:
    x = randint(20, 35)
    if x>32:
        ile += 1
    i += 1
print(ile)
