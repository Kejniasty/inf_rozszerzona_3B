import random

a=[]
i = random.randrange(2, 51)
a.append(i)
while (i%7!=0):
    i = random.randrange(2, 51)
    a.append(i)

a.sort()
last = len(a)-1
print(a[last])

s=0
for i in a:
    s+=i

print(s)
