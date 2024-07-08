names = locals()

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

name  = 'CG2R61'


charge = 0.00215
charge = str('%.5f' % charge)


c_lo = '-' + charge
c_up = charge

for line in r2:
    ls = line.split()

    for i in range(8):
        names['l_' + str(i + 1)] = ls[i]

    if ls[1] == name:
        if ls[2] == '1':
            l_7 = c_lo

    if ls[1] == name:
        if ls[2] == '2':
            l_7 = c_up

    line_new = ''
    for i in range(8):
        lenn = names['kp' + str(i + 1)] - len(names['l_' + str(i + 1)])
        for j in range(lenn):
            line_new += ' '
        line_new += names['l_' + str(i + 1)]

    print(line_new)


