x = int(input())
y = int(input())
z = 5
x += 2
if x<y:
    x *= z
    y -= 1
else:
    if x==y:
        y -= z
        x -= 1
    else:
        y += z
        x += 1

print(x, y)
