from math import floor
res = 3840 * 2160
i = 24
I = 32 * 8 * 1024 * 1024 * 1024
k = 13269234531
I1 = floor(I / i / res)
print(k/I1)