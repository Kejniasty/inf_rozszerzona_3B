n =int(input())
s = 0
for i in range(n):
     s+=i

print(2*n/s)

s=0
for i in range(1, n+1):
    s += 1/(2*i)

print(s)
