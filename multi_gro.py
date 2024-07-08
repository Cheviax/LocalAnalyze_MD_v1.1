names = locals()
readd = open('D:/mysql/allNAdt5.gro', 'r')

lines = readd.readlines()
steps_all = 6000
#
steps = 0

bd2 = 10.65819 / 2
bb = 10.65819

for line in lines:
    ls = line.split()
    if len(ls) == 5:
        steps = int(float(ls[2]))
        names['step_'+str(steps)] = []
        if steps % 100 == 0:
            print(steps)

    if len(ls) == 6:
        num = line[0:5]
        xx = ls[3]
        yy = ls[4]
        zz = ls[5]
        line_new = num+' '+xx+' '+yy+' '+zz
        names['step_'+str(steps)].append(line_new)

for i in step_0:
    iss = i.split()
    num = iss[0]
    names[str(num) + '_wrt'] = open('H:/PY_OUT/num_'+str(num)+'.txt', 'w')
    names[str(num) + '_xx0'] = float(iss[1])
    names[str(num) + '_yy0'] = float(iss[2])
    names[str(num) + '_zz0'] = float(iss[3])

for j in range(steps_all):
    steps = str(5 + j*5)
    name = 'step_'+steps
    wrt_step = open('H:/PY_OUT/step_'+steps+'.txt', 'w')

    if float(steps) % 100 == 0:
        print(steps)

    for i in names[name]:
        iss = i.split()
        num = iss[0]
        xxt = float(iss[1])
        yyt = float(iss[2])
        zzt = float(iss[3])

        dx = abs(xxt - names[str(num) + '_xx0'])
        dy = abs(yyt - names[str(num) + '_yy0'])
        dz = abs(zzt - names[str(num) + '_zz0'])

        if dx > bd2:
            dx = bb - dx
        if dy > bd2:
            dy = bb - dy
        if dz > bd2:
            dz = bb - dz

        ds = (dx**2+dy**2+dz**2) ** 0.5

        wrt_step.write(str(ds)+'\n')
        names[str(num) + '_wrt'].write(str(ds)+'\n')

        names[str(num) + '_xx0'] = float(iss[1])
        names[str(num) + '_yy0'] = float(iss[2])
        names[str(num) + '_zz0'] = float(iss[3])