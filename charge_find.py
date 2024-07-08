names = locals()

rd = open('nio_gro.txt', 'r')
rd = rd.readlines()
r2 = open('nio_top.txt', 'r')
r2 = r2.readlines()

kp1 = 6
kp2 = 11
kp3 = 7
kp4 = 7
kp5 = 7
kp6 = 7
kp7 = 11
kp8 = 11

z_lo = []
z_up = []

lo_num = 0
up_num = 0

for line in rd:
    ls = line.split()
    if float(ls[5]) == 0.51:
        z_lo.append(ls[2])
        lo_num += 1

    if float(ls[5]) == 10.51:
        z_up.append(ls[2])
        up_num += 1

print(lo_num)
print(up_num)

charge = 0.016
charge = str('%.4f' % charge)


c_lo = charge
c_up = '-' + charge

for line in r2:
    ls = line.split()

    for i in range(8):
        names['l_' + str(i + 1)] = ls[i]

    if ls[0] in z_lo:
        l_7 = c_up

    if ls[0] in z_up:
        l_7 = c_lo

    line_new = ''
    for i in range(8):
        lenn = names['kp' + str(i + 1)] - len(names['l_' + str(i + 1)])
        for j in range(lenn):
            line_new += ' '
        line_new += names['l_' + str(i + 1)]

    print(line_new)


