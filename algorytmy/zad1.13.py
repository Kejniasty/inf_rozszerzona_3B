import cmath
print("Ax^2 + Bx + C = 0")
print("Podaj A")
quadratic_coefficient = float(input())
print("Podaj B")
linear_coefficient = float(input())
print("Podaj C")
constant_term = float(input())
discriminant = linear_coefficient**2 - 4*quadratic_coefficient*constant_term
first_root = (-linear_coefficient -
              cmath.sqrt(discriminant))/2*quadratic_coefficient
second_root = (-linear_coefficient +
              cmath.sqrt(discriminant))/2*quadratic_coefficient

print(first_root, second_root)
