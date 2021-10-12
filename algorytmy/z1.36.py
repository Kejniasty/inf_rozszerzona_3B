def fact(n):
    if n==1 or n==0:
        return 1
    elif n==2:
        return 2
    else:
        return n*fact(n-1)

n = int(input())
k = int(input())
num = fact(n)
den = fact(k) * fact(n-k)
print(num/den)
