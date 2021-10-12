import math

def if_triangle_exists(a, b, c):
    if (a+b) < c or (a+c) < b or (b+c) < a:
        return False
    else:
        return True

'''while True:
    try:'''
        
'''        break
    except ValueError:
        print("Podano błędne dane wejściowe, spróbuj ponownie")''''

print("Podaj pierwszy bok")
first_side = int(input())
print("Podaj drugi bok")
second_side = int(input())
print("Podaj trzeci bok")
third_side = int(input())
if if_triangle_exists(first_side, second_side, third_side) or first_side < 0 or second_side < 0 or third_side < 0:
    raise ValueError

p = (first_side + second_side + third_side)/2
area = (p*(p-first_side)*(p-(second_side)*(p-third_side))**(0.5)
print(area)
