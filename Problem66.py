'''
Diophantine Equation (25%)
6/12/19
158ms
'''

import time
import math
import re

start_time = time.perf_counter()

# Finding continued fraction sequence

max_n = 0
max_x = 0

for n in range(2, 1001):
    if int(math.sqrt(n) + 0.5) ** 2 == n:
        continue

    # print('n ' + str(n))
    seq = []
    repeat = []
    floor = 0
    numerConst = 0
    denom = 1

    while True:
        floor = int((math.sqrt(n) + numerConst) / denom)
        numerConst = int(-(numerConst - floor * denom))
        denom = int((n - numerConst ** 2) / denom)
        string = str(floor) + ',' + str(numerConst) + ',' + str(denom)
        if string in seq:
            index = seq.index(string)
            while len(seq) > index:
                repeat.append(int(re.search('[0-9]+', seq.pop(index)).group()))
            for i in range(len(seq)):
                seq.append(
                    int(re.search('[0-9]+', seq.pop(len(seq) - 1)).group())
                )
            break

        seq.append(string)

    limit = 2
    continued = seq.copy()
    while len(continued) < limit:
        elem = repeat.pop(0)
        continued.append(elem)
        repeat.append(elem)

    while True:
        # Calculating approximate fractions
        numerator = 1
        denominator = continued[limit - 1]

        for i in range(limit - 2, -1, -1):
            numerator += continued[i] * denominator
            if i != 0:
                temp = numerator
                numerator = denominator
                denominator = temp

        # Check in Diophantine equation
        if numerator ** 2 == n * (denominator ** 2) + 1:
            if numerator > max_x:
                max_x = numerator
                max_n = n
            break
        elem = repeat.pop(0)
        continued.append(elem)
        repeat.append(elem)
        limit += 1

print(max_n)
end_time = time.perf_counter()

print('ms: ' + '{:.0f}'.format((end_time - start_time) * 1000))
