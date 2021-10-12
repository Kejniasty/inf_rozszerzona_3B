n = int(input())

for i in range(n):
    print(3*2**i)
print('\n')

for i in range(n):
    if i%2 == 0:
        print(3*2**i)
    else:
        print(-3*2**i)
print('\n')
s=0
for i in range(0, n):
    s += -10 + 6*i
    
print(s)
print('\n')
il=1
for i in range(0, n):
    il *= (-2)**i
    
print(il)
    
