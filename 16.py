from sys import setrecursionlimit
setrecursionlimit(10**8)

def f(n):
    if n % 2 == 0:
        return f(n//2) + 3
    if n % 2 != 0 and n % 3 == 0:
        return f(n//3) + 2
    if n % 2 != 0 and n % 3 != 0:
        return 0
for n in range(2,10000000,2):
    if f(n) == 65:
        print(n)