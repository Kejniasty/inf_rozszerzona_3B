def pot(a, b):
    if b==0:
        return 1
    else:
        return a*pot(a, b-1)

def seq(n):
    if n==1:
        return 1
    else:
        return ((-n)*seq(n-1) + 4)


