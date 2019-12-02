import math
import time

start_time = time.perf_counter()

count = 0

for n in range(2, 10001):
    if int(math.sqrt(n) + 0.5) ** 2 == n:
        continue
    seq = []
    floor = 0
    numerConst = 0
    denom = 1

    i = 0
    while True:
        floor = int((math.sqrt(n) + numerConst) / denom)
        numerConst = -(numerConst - floor * denom)
        denom = (n - numerConst ** 2) / denom
        string = str(floor) + str(numerConst) + str(denom)

        if string in seq:
            if (i - seq.index(string)) % 2 == 1:
                count += 1
            break

        seq.append(string)
        i += 1

print(count)

end_time = time.perf_counter()
print('{:.0f}'.format((end_time - start_time) * 1000) + 'ms')
