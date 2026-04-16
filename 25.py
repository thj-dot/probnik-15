from fnmatch import fnmatch
a = []
for i in range(0,10**9,8587):
    if fnmatch(str(i),'?05*22*3'):
        a.append(i)
def sm(n):
    sm = 0
    for x in str(n):
        sm += int(x)
    return sm

a.sort(key=lambda x: sm(x))
for x in a:
    print(sm(x))
print(a)
