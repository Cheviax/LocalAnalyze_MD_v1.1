names = locals()



x_b = 2.39
x_e = 5.39
d = x_e - x_b
rb = d * -0.505

zhen = 50000
sl   = 100

vv = (11.3 - 6) * d / sl
cc = 1.66

for i in range(sl):
    names['li'+str(i+1)] = 0
    names['mg'+str(i+1)] = 0
    names['cl'+str(i+1)] = 0
    names['iff'+str(i+1)] = x_b + d / sl * (i+1)

for j in range(zhen):
    red = open('H:/GMX_OUT/concentration/ion' + str(j) + '.gro', 'r')

    lines = red.readlines()
    del lines[0]
    del lines[0]
    del lines[-1]
    del lines[-1]
    for line in lines:
        ls = line.split()
        atom = ls[1]
        xx = ls[3]
        zz = ls[5]
        if (float(zz) > 6.5) and (float(zz) < 10.8):
            for i in range(sl):
                if float(xx) <= names['iff'+str(i+1)]:
                    if atom == 'LI':
                        names['li'+str(i+1)] += 1
                    elif atom == 'MG':
                        names['mg'+str(i+1)] += 1
                    else:
                        names['cl'+str(i+1)] += 1
                    break

print('ok')
for i in range(sl):
    names['li' + str(i + 1)] = names['li' + str(i + 1)] / zhen / vv * cc
    names['mg' + str(i + 1)] = names['mg' + str(i + 1)] / zhen / vv * cc
    names['cl' + str(i + 1)] = names['cl' + str(i + 1)] / zhen / vv * cc
    dr = d / 100
    rb += dr
    linenew = str('%.3f' % (rb))+ ' ' + str(names['li' + str(i + 1)])+' '+str(names['mg' + str(i + 1)])+' '+str(names['cl'+str(i+1)])
    print(linenew)