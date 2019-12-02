'''
Totient Maximum (10%)
6/19/19
0ms
'''

import time
import math

start_time = time.perf_counter()

limit = 100
primes = []
for i in range(2, limit + 1):
    primes.append(i)
for i in range(2, int(math.sqrt(limit))):
    if i in primes:
        for j in range(i * 2, limit + 1, i):
            if j in primes:
                primes.remove(j)

num = 1
new = 1
for i in range(0, len(primes) + 1):
    new *= primes[i]
    if new > 1000000:
        print(num)
        break
    num = new

end_time = time.perf_counter()

print('ms: ' + '{:.0f}'.format((end_time - start_time) * 1000))
