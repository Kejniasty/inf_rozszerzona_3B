n = int(input())
print(2**n - 1)
a = []
for _ in range(n):
    a.append(0)

if n%2==0:
    for _ in range(0, 2**n-1, 3):
        print("A <-> B")
        print("A <-> C")
        print("B <-> C")
else:
    for _ in range(0, 2**n-1, 3):
        print("A <-> C")
        print("A <-> B")
        print("B <-> C")
    
    
