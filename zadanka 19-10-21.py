#                                        "Bartek Kubik 3B"

"schemat blokowy"

n = int(input("Podaj N: "))
i = 1
p = 1
while i <= n:
    p = p * i
    i = i +1

print(p)

"zadanie 1"

import math

a = float(4.25)
b = float(3)
gora = float(a * (b ** 2))
dol = float(3 * math.sqrt(a))

w = gora / dol

print(w)

"zadanie 2"

a = int(input("Podaj A: "))
b = int(input("Podaj B: "))
c = int(input("Podaj C: "))

if a > b:
    if b > c:
        print("c jest najmniejsza")
    else:
        if a > c:
            print("c jest najmniejsza")
        else:
            print("b jest najminejsza")
else:
    if a > c:
        print("c jest najmniejsza")
    else:
        print("a jest najminejsza")

"zadanie 3"

import math

a = int(input("Podaj bok A: "))
b = int(input("Podaj bok B: "))
c = int(input("Podaj bok C: "))

p = (a + b + c)/2
pole = math.sqrt(p*(p-a)*(p-b)*(p-c))

print(p)

"zadanie 4"

print("Podaj liczby nie większe od 40")
a = int(input("Podaj liczbę A: "))
b = int(input("Podaj liczbę B: "))

if a > 40 or b > 40:
    print("miało być nie większe od 40 :(")
else:
    print(a * b)

"zadanie 5"

x = -3
for i in range(5):
    print(x)
    x = x * -2

"zadanie 6"

z = int(input("Podaj długość ciągu: "))
x = -10
s = 0

for i in range(z):
    s = s + x
    x = x + 6

print(s)