from math import dist
a = open('27-78b.txt').readlines()
for i in range(len(a)):
    a[i] = a[i].replace(',','.')
    x, y = a[i].split()
    a[i] = [float(x), float(y)]
def cluster():
    k = [a.pop(0)]
    el = k[0]
    for el in k:
        for x in a[::]:
            if dist(x, el) < 1:
                k.append(x)
                a.remove(x)
    return k
clusters = []
while len(a) > 0:
    cl = cluster()
    if len(cl) > 0:
        clusters.append(cl)
def center(K):
    c = 0
    mns = 0
    for t1 in K:
        sm = 0
        for t2 in K:
            sm += dist(t1,t2)
        if sm < mns:
            mns = sm
            c = t1
    return c
R1 = 0.0
R2 = 0.0
R3 = 0.0
R4 = 0.0
K1 = clusters[0]
K2 = clusters[1]
K3 = clusters[2]
K4 = clusters[3]
C1 = center(clusters[0])
C2 = center(clusters[1])
C3 = center(clusters[2])
C4 = center(clusters[3])
for x in K1:
    if dist(C1,x) > R1:
        R1 = dist(C1,x)
for x in K2:
    if dist(C2,x) > R2:
        R2 = dist(C2,x)
for x in K3:
    if dist(C3,x) > R3:
        R3 = dist(C3,x)
for x in K4:
    if dist(C4,x) > R4:
        R4 = dist(C4,x)
R = (R1 + R2 + R3 + R4) / 4 * 10000
print(R)