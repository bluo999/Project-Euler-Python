count = 0

for i in range(1, 101):
    for j in range(1, 101):
        num = i ** j
        if len(str(num)) > j:
            break
        if len(str(num)) == j:
            count += 1

print(count)
