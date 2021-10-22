print("y = kx + b1; y = mx + b2")
k = float(input("k: "))
m = float(input("m: "))
b1 = float(input("b1: "))
b2 = float(input("b2: "))
if k==m and b1==b2:
    print("Proste się na siebie nachodzą")
elif k==m and b1!=b2:
    print("Proste są równoległe")
elif k*m==-1:
    print("Proste są prostopadłe")
else:
    print("nie ma zależności między prostymi")
