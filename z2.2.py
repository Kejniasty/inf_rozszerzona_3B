print("Ax + By + C = 0")
A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))
print("Odcinek AB, A(x, y), B(m, n)")
x = float(input("x: "))
y = float(input("y: "))
m = float(input("m: "))
n = float(input("n: "))

a1 = round(-(A/B), 10)
b1 = round(-(C/B), 10)

a2 = round((y - n)/(x - m), 10)
b2 = round(y - a2*x, 10)

print(a1, " ", b1)
print(a2, " ", b2)

if a1==a2 and b1==b2:
    print("Odcinek leży na prostej")
else:
    print("Odcinek nie leży na prostej")
