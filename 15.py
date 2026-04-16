P = [57892, 478683]
Q = [123456, 760123]
R = [592916, 977654]
def p(x):
    return P[0] <= x <= P[1]
def q(x):
    return Q[0] <= x <= Q[1]
def r(x):
    return R[0] <= x <= R[1]
c = sorted(list(set(P + Q + R)))
a = []
for i in range(len(c) - 1):
    lt, rt = c[i], c[i + 1]
    x = (lt + rt) / 2
    f = (q(x)) <= ((not p(x)) <= ((not r(x) and not False) <= (not q(x))))
    if not f:
        a.append((lt, rt))
if a:
    print(a[-1][1] - a[0][0])
else:
    print(0)