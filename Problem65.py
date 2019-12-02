limit = 100
Continued = []
Continued.append(2)

for i in range(1, limit):
    if i % 3 == 0 or i % 3 == 1:
        Continued.append(1)
    else:
        Continued.append(2 * (i + 1) / 3)

numerator = 1
denominator = Continued[limit - 1]

for i in range(limit - 2, -1, -1):
    numerator += Continued.pop(i) * denominator
    if i != 0:
        temp = numerator
        numerator = denominator
        denominator = temp

total = 0
for c in str(int(numerator)):
    total += int(c)

print(total)
