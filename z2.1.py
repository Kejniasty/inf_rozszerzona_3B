print("Podaj Ax+By+C = 0")
A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))
print("Podaj punkt P(m, n)")
m = float(input("m: "))
n = float(input("n: "))
distance = abs(A*m + B*n + C)/((A**2 + B**2)**0.5)
print(distance)