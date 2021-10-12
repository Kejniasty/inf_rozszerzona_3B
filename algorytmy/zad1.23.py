n = int(input())
s=0
for i in range(n):
    s += (-1)**(i+1) * (2 + 3*i)

print(s)

num = 1
den = 1
for i in range(n):
    num *= 2 + 0.5*i
    den *= -3  * 10**(-i)

print(num/den)

num = 1
den = 1
for i in range(1, n+1):
    num += (-1)**i * (2 + 5*i)
    den *= (-1)**(i+1) * (3 + 4*i)

print(num/den)
