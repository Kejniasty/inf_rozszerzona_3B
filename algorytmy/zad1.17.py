import math

x = int(input())
if x<7:
    print(x**3 + 1)
elif x==7:
    print(math.cos(x-1))
elif x==9:
    print(math.sqrt(3*x))
else:
    print(-8*x)
