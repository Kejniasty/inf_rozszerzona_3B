ilo = 1
nums = []
while (ilo<10000):
    a = int(input())
    nums.append(a)
    ilo *= a

n = nums.count(0)
for _ in range(n):
    nums.remove(0)

print(len(nums))
print(ilo)
