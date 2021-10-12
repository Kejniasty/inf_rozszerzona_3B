def seq1(n):
    if n==1:
        return 2
    else:
        return 3*seq1(n-1) + 0.5

def seq2(n):
    if n==1:
        return 2
    elif n==2:
        return -4
    else:
        return seq2(n-2) + 2*seq2(n-1) + 0.5

for i in range(1, 8):
    print(seq1(i))
   
for i in range(1, 8):
    print(seq2(i))

n=int(input())
print(seq1(n))
print(seq2(n))
