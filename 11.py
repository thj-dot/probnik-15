from math import log2, ceil
N = 8164+52
k = 835
i = ceil(log2(N))
I = 156 * 8 * 1024
for l in range(1000000):
    I1 = ceil(i * l)
    if I1 * k > I:
        print(l)
        break