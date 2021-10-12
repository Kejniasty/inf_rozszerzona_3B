def seq1(n):
    if n==1:
        return 2
    else:
        return 2*seq1(n-1)

def seq2(n):
    if n==1:
        return 3
    if n==2:
        return 5
    else:
        return 1 + seq2(n-2)

print(seq1(10))
print(seq2(8))

