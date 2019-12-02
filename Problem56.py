maxSum = 0

for a in range(1, 100):
    for b in range(1, 100):
        total = 0
        exp = str(a ** b)
        for c in exp:
            total += int(c)
        if total > maxSum:
            maxSum = total

print(maxSum)
