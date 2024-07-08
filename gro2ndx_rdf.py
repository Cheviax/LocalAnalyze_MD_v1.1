
names = locals()

zhen = 100
R_box = 2.55
D_box = 5.10

z_max = 10.392
r_range = 3
r_co_1 = 0.6
r_co_2 = 0.6

def take_one(ele):
    return ele[0]

for i in range(zhen):
    names['hyd_'+str(i)] = []
    names['cyc_'+str(i)] = []
    names['sol_'+str(i)] = []
    names['acn_'+str(i)] = []

sys = '05-2'

for i in range(zhen):
    file_1 = open('F:/GMX/gong-hjt/oplsaa/re_1202/nvt-'+sys+'-hyd-' + str(i) + '.gro', 'r')
    file_2 = open('F:/GMX/gong-hjt/oplsaa/re_1202/nvt-'+sys+'-cyc-' + str(i) + '.gro', 'r')
    file_3 = open('F:/GMX/gong-hjt/oplsaa/re_1202/nvt-'+sys+'-water-' + str(i) + '.gro', 'r')
    file_4 = open('F:/GMX/gong-hjt/oplsaa/re_1202/nvt-'+sys+'-acn-' + str(i) + '.gro', 'r')

    lines = file_1.readlines()
    del lines[0]
    del lines[0]
    del lines[-1]
    line_count = 0
    iff = 0
    for line in lines:
        line_count += 1
        if line_count == 2:
            xx = float(line[21:28])
            yy = float(line[29:36])
            zz = float(line[37:44])
            if zz >= (z_max - r_range):
                eo1 = [xx, yy, zz]
                iff += 1
        if line_count == 3:
            if iff == 1:
                xx = float(line[21:28])
                yy = float(line[29:36])
                zz = float(line[37:44])
                eo2 = [xx, yy, zz]
                iff += 1
        if iff == 2:
            iff = 0
            xi = (eo1[0]+eo2[0])/2
            yi = (eo1[1]+eo2[1])/2
            zi = (eo1[2]+eo2[2])/2
            eoi = [xi, yi, zi]
            names['hyd_' + str(i)].append(eoi)

        if line_count == 4:
            line_count = 0

    lines = file_2.readlines()
    del lines[0]
    del lines[0]
    del lines[-1]
    line_count = 0
    iff = 0
    for line in lines:
        line_count += 1
        if line_count == 2:
            xx = float(line[21:28])
            yy = float(line[29:36])
            zz = float(line[37:44])
            if zz >= (z_max - r_range):
                eo1 = [xx, yy, zz]
                iff += 1
        if line_count == 9:
            if iff == 1:
                xx = float(line[21:28])
                yy = float(line[29:36])
                zz = float(line[37:44])
                eo2 = [xx, yy, zz]
                iff += 1
        if iff == 2:
            iff = 0
            xi = (eo1[0] + eo2[0]) / 2
            yi = (eo1[1] + eo2[1]) / 2
            zi = (eo1[2] + eo2[2]) / 2
            eoi = [xi, yi, zi]
            names['cyc_' + str(i)].append(eoi)

        if line_count == 17:
            line_count = 0

    lines = file_3.readlines()
    del lines[0]
    del lines[0]
    del lines[-1]
    line_count = 0
    for line in lines:
        line_count += 1
        if line_count == 4:
            xx = float(line[21:28])
            yy = float(line[29:36])
            zz = float(line[37:44])
            if zz >= (z_max - r_range - r_co_2):
                eoi = [xx, yy, zz]
                names['sol_' + str(i)].append(eoi)
        if line_count == 4:
            line_count = 0

    lines = file_4.readlines()
    del lines[0]
    del lines[0]
    del lines[-1]
    line_count = 0
    iff = 0
    for line in lines:
        line_count += 1
        if line_count == 2:
            xx = float(line[21:28])
            yy = float(line[29:36])
            zz = float(line[37:44])
            if zz >= (z_max - r_range - r_co_2):
                eo1 = [xx, yy, zz]
                iff += 1
        if line_count == 3:
            if iff == 1:
                xx = float(line[21:28])
                yy = float(line[29:36])
                zz = float(line[37:44])
                eo2 = [xx, yy, zz]
                iff += 1
        if iff == 2:
            iff = 0
            xi = (eo1[0] + eo2[0]) / 2
            yi = (eo1[1] + eo2[1]) / 2
            zi = (eo1[2] + eo2[2]) / 2
            eoi = [xi, yi, zi]
            names['acn_' + str(i)].append(eoi)
        if line_count == 6:
            line_count = 0

    print(len(names['hyd_' + str(i)]))
    print(len(names['cyc_' + str(i)]))
    print(len(names['sol_' + str(i)]))
    print(len(names['acn_' + str(i)]))
    print('-------------------------')

print('         ALL  SOL  ACN  NONE')
count_hyd_a = 0
count_hyd_0 = 0
count_hyd_1 = 0
count_hyd_2 = 0
count_cyc_a = 0
count_cyc_0 = 0
count_cyc_1 = 0
count_cyc_2 = 0

for i in range(zhen):
    num_hyd_0 = 0
    num_hyd_1 = 0
    num_hyd_2 = 0
    for xyz in names['hyd_'+str(i)]:
        xi = xyz[0]
        yi = xyz[1]
        zi = xyz[2]
        count = 0
        if_0 = 0
        if_1 = 0
        for abc in names['sol_'+str(i)]:
            xj = abc[0]
            yj = abc[1]
            zj = abc[2]
            dx = abs(xi - xj)
            dy = abs(yi - yj)
            dz = abs(zi - zj)
            if dx >= R_box:
                dx = D_box - dx
            if dy >= R_box:
                dy = D_box - dy
            dd =  ((dx ** 2) + (dy ** 2) + (dz ** 2)) ** 0.5
            if dd < r_co_1:
                count += 1
            if count >= 8:
                num_hyd_0 += 1
                if_0 = 1
                break
        count = 0
        for abc in names['acn_'+str(i)]:
            xj = abc[0]
            yj = abc[1]
            zj = abc[2]
            dx = abs(xi - xj)
            dy = abs(yi - yj)
            dz = abs(zi - zj)
            if dx >= R_box:
                dx = D_box - dx
            if dy >= R_box:
                dy = D_box - dy
            dd =  ((dx ** 2) + (dy ** 2) + (dz ** 2)) ** 0.5
            if dd < r_co_1:
                count += 1
            if count >= 8:
                num_hyd_1 += 1
                if_1 = 1
                break

        if (if_0 == 0) and (if_1 == 0):
            num_hyd_2 += 1

    print(str(i)+': HYD: '+str(len(names['hyd_'+str(i)]))+'    '+str(num_hyd_0)+'    '+str(num_hyd_1)+'    '+str(num_hyd_2))

    num_cyc_0 = 0
    num_cyc_1 = 0
    num_cyc_2 = 0
    for xyz in names['cyc_'+str(i)]:
        xi = xyz[0]
        yi = xyz[1]
        zi = xyz[2]
        count = 0
        if_0 = 0
        if_1 = 0

        for abc in names['sol_'+str(i)]:
            xj = abc[0]
            yj = abc[1]
            zj = abc[2]
            dx = abs(xi - xj)
            dy = abs(yi - yj)
            dz = abs(zi - zj)
            if dx >= R_box:
                dx = D_box - dx
            if dy >= R_box:
                dy = D_box - dy
            dd =  ((dx ** 2) + (dy ** 2) + (dz ** 2)) ** 0.5
            if dd < r_co_2:
                count += 1
            if count >= 8:
                num_cyc_0 += 1
                if_0 = 1
                break
        count = 0
        for abc in names['acn_'+str(i)]:
            xj = abc[0]
            yj = abc[1]
            zj = abc[2]
            dx = abs(xi - xj)
            dy = abs(yi - yj)
            dz = abs(zi - zj)
            if dx >= R_box:
                dx = D_box - dx
            if dy >= R_box:
                dy = D_box - dy
            dd =  ((dx ** 2) + (dy ** 2) + (dz ** 2)) ** 0.5
            if dd < r_co_2:
                count += 1
            if count >= 8:
                num_cyc_1 += 1
                if_1 = 1
                break

        if (if_0 == 0) and (if_1 == 0):
            num_cyc_2 += 1

    print(str(i)+': CYC:  '+str(len(names['cyc_'+str(i)]))+'    '+str(num_cyc_0)+'    '+str(num_cyc_1)+'    '+str(num_cyc_2))
    count_hyd_a += len(names['hyd_'+str(i)])
    count_hyd_0 += num_hyd_0
    count_hyd_1 += num_hyd_1
    count_hyd_2 += num_hyd_2
    count_cyc_a += len(names['cyc_' + str(i)])
    count_cyc_0 += num_cyc_0
    count_cyc_1 += num_cyc_1
    count_cyc_2 += num_cyc_2

count_hyd_a /= zhen
count_hyd_0 /= zhen
count_hyd_1 /= zhen
count_hyd_2 /= zhen
count_cyc_a /= zhen
count_cyc_0 /= zhen
count_cyc_1 /= zhen
count_cyc_2 /= zhen

print('HYD all: '+str(count_hyd_a)+' '+'in water: '+str(count_hyd_0)+' '+'in ACN: '+str(count_hyd_1)+' '+'other: '+str(count_hyd_2))
print('CYC all: '+str(count_cyc_a)+' '+'in water: '+str(count_cyc_0)+' '+'in ACN: '+str(count_cyc_1)+' '+'other: '+str(count_cyc_2))

