a = float(input())
b = float(input())
if a>b:
    print("B jest mniejsza")
elif b<a:
    print("a jest mniejsza")
else:
    print("równe")


a = float(input())
b = float(input())
if a<0 or b<0:
    print("Taki prostokąt nie istnieje")
else:
    print(a*b)


a = float(input())
b = float(input())
c = float(input())
if a==0:
    print("taka prosta nie istnieje")
else:
    print((c-b)/a)


a = int(input())
if a%2==0:
    print("Tak")
else:
    print("Nie")
    

a = int(input())
b = int(input())
if a==0 and b==0:
    print("tożsamość")
elif a==0 and b!=0:
    print("sprzeczność")
else:
    print(-b/a)
    
    
a = int(input())
b = int(input())
if a>=12 and b>=20:
    print("kup bilet")
if a<12 or b>=20:
    print("możesz wejść")
if not a>7:
    print("wejdź za darmo")