def sh(n):
    a = []
    while n > 0:
        a.append(n%6)
        n //= 6
    return len(a)
def d(n):
    a = []
    while n > 0:
        a.append(n%9)
        n //= 9
    return len(a)



s = open('17-418.txt').readlines()
a = []
for x in s:
    a.append(int(x))
mnsh = 100000
mnd = 100000
for x in a:
    if sh(x) == 4:
        mnsh = min(mnsh,x)
    if d(x) == 3:
        mnd = min(mnd,x)
mxs = 0
k = 0
for i in range(len(a)-1):
    a1, a2 = a[i], a[i+1]
    sm = a1 + a2
    if a1 % 11 == mnsh % 5 or a2 % 11 == mnsh % 5:
        if a1 % 7 == mnd % 13 or a2 % 7 == mnd % 13:
            k += 1
            mxs = max(mxs, sm)
print(k,mxs)