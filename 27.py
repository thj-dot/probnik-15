from math import dist
def center(K):
    c = 0
    mns = 100000
    for t1 in K:
        sm = 0
        for t2 in K:
            sm += dist(t1,t2)
        if sm < mns:
            mns = sm
            c = t1
    return c
def cluster():
    k = [a.pop(0)]
    el = k[0]
    for el in k:
        for x in a[::]:
            if dist(el,x) < 1:
                k.append(x)
                a.remove(x)
    return k

a = open('27-78a.txt').readlines()
for i in range(len(a)):
    a[i] = a[i].replace(',','.')
    x, y = a[i].split()
    a[i] = [float(x), float(y)]
clusters = []
while len(a) != 0:
    cl = cluster()
    if len(cl) > 0:
        clusters.append(cl)
K1 = clusters[0]
K2 = clusters[1]
C1 = center(clusters[0])
C2 = center(clusters[1])
R1 = 0.0
R2 = 0.0
for x in K1:
    if dist(C1,x) > R1:
        R1 = dist(C1,x)
for x in K2:
    if dist(C2,x) > R2:
        R2 = dist(C2,x)
R = (R1 + R2) / 2  * 10000
print(R)