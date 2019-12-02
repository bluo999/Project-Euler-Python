'''
Magic 5-gon Ring (25%)
6/19/19
95ms
'''

import time


class GonRing:

    size = 0
    total = 0
    outer = None
    inner = None
    inside_sum = 0

    def __init__(self, size, total):
        self.size = size
        self.total = total
        self.outer = []
        self.inner = []
        self.inside_sum = int(size * total - (2 * size) * (2 * size + 1) / 2)

    def __repr__(self):
        string = ''
        for i in range(0, self.size):
            string += (str(self.outer[i]) + str(self.inner[i]) +
                       str(self.inner[(i + 1) % self.size]))
        return string

    def set_total(self, total):
        self.total = total
        self.inside_sum = int(size * total - (2 * size) * (2 * size + 1) / 2)

    def used_set(self):
        return set(self.outer).union(self.inner)

    def clear(self):
        self.outer.clear()
        self.inner.clear()

    def fill(self):
        save_inner = self.inner.copy()
        save_outer = self.outer.copy()

        changed = True

        while (changed):
            if len(self.inner) == self.size and len(self.outer) == self.size:
                return True

            changed = False
            if len(self.outer) == len(self.inner):
                length = len(self.outer)
                num = total - self.outer[length - 1] - self.inner[length - 1]
                if ((num in range(1, self.size * 2 + 1) and
                     num not in self.used_set())):
                    self.inner.append(num)
                    changed = True
                else:
                    self.inner = save_inner
                    self.outer = save_outer
                    return False

            elif len(self.inner) == size - 1:
                num = self.inside_sum
                for i in self.inner:
                    num -= i
                if ((num in range(1, self.size * 2 + 1) and
                     num not in self.used_set())):
                    self.inner.append(num)
                    changed = True
                else:
                    self.inner = save_inner
                    self.outer = save_outer
                    return False

            elif ((len(self.inner) >= len(self.outer) + 2 or
                   (len(self.outer) == size - 1 and
                    len(self.inner) >= len(self.outer) + 1))):
                length = len(self.outer)

                num = total - (self.inner[(length + 1) % self.size] +
                               self.inner[length])

                if ((num in range(self.outer[0], self.size * 2 + 1) and
                     num not in self.used_set())):
                    self.outer.append(num)
                    ''' last_sum = self.inner[size - 1] + self.inner[size - 2]
                    if ((length == size - 1)):  # and
                        # last_sum + self.outer[size - 1] != total)):
                        self.inner = save_inner
                        self.outer = save_outer
                        return False'''
                    changed = True
                else:
                    self.inner = save_inner
                    self.outer = save_outer
                    return False

        return True


start_time = time.perf_counter()

max_str = 0
size = 5
ring = GonRing(size, 1)
for total in range(1, 20):
    ring.set_total(total)
    for i in range(1, size * 2 + 1):
        for j in range(1, size * 2 + 1):
            ring.outer.append(i)
            if j in ring.used_set():
                ring.clear()
                continue
            ring.inner.append(j)
            if ring.fill():
                for k in range(1, size * 2 + 1):
                    if k in ring.used_set():
                        continue
                    ring.inner.append(k)
                    if ring.fill():
                        for l in range(1, size * 2 + 1):
                            if l in ring.used_set():
                                continue
                            ring.inner.append(l)
                            if ring.fill():
                                ring_str = str(ring)
                                if len(ring_str) == 16 and int(ring_str) > max_str:
                                    max_str = int(ring_str)
                            ring.inner.pop()
                    ring.inner.pop()
            ring.clear()

print(max_str)

end_time = time.perf_counter()

print('ms: ' + '{:.0f}'.format((end_time - start_time) * 1000))
