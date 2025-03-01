n = list(map(int, input().split()))
num = n[0]
m = n[0]

for i in n[1:]:
    if i > num:
        num = i

for j in n[1:]:
    if j != num and j > m:
        m = j
print(m)
