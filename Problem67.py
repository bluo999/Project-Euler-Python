'''
Maximum Path Sum II (5%)
6/13/19
9ms
'''

import time

start_time = time.perf_counter()

tree = {}

i = 0
with open('Problem67Input', 'r') as file:
    for line in file:
        value = list(map(int, line.split()))
        tree[i] = value
        i += 1

rows = i
for i in range(rows - 2, -1, -1):
    for j in range(len(tree[i])):
        tree[i][j] += max(tree[i + 1][j], tree[i + 1][j + 1])

print(tree[0][0])

end_time = time.perf_counter()

print('ms: ' + '{:.0f}'.format((end_time - start_time) * 1000))
