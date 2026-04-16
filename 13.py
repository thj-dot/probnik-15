from ipaddress import ip_network
ip = '193.18.135.201'
for i in range(32):
    count = 0
    m = i * '1' + '0' * (32 - i)
    x1, x2, x3, x4 = m[0:8], m[8:16], m[16:24], m[24:32]
    mask = str(int(x1,2)) + '.' + str(int(x2,2)) + '.' + str(int(x3,2)) + '.' + str(int(x4,2))
    net = ip_network(f'{ip}/{mask}',strict=False)
    for a in net:
        if bin(int(a)).count('1') == 19:
            count += 1
    if count == 105:
        print(32-i)
        break