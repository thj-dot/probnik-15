a = open('24_28765.txt').readline()
import sys
sys.set_int_max_str_digits(10**6)

mx = 0
ind = 0
curr = ''
st = 0
A = '0123456789ABCD'
for i in range(len(a)):
    if a[i] in A:
        curr += a[i]
    else:
        if len(curr) != 0:
            if int(curr,14) > mx and int(curr,14) % 2 == 0:
                mx = int(curr,14)
                ind = st
        curr = ''
        st = i
print(ind)