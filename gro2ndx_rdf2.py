import time

names = locals()

zhen = 100
R_box = 2.55
D_box = 5.10

z_max = 10.392
r_range = 3
r_co = 0.5

def take_one(ele):
    return ele[0]

for i in range(zhen):
    names['hyd_'+str(i)] = []
    names['cyc_'+str(i)] = []
    names['sol_'+str(i)] = []
    names['acn_'+str(i)] = []

for i in range(zhen):
    file_1 = open('F:/GMX/gong-hjt/oplsaa/re_1202/nvt-03-1-hyd-' + str(i) + '.gro', 'r')
    file_2 = open('F:/GMX/gong-hjt/oplsaa/re_1202/nvt-03-1-cyc-' + str(i) + '.gro', 'r')
    file_3 = open('F:/GMX/gong-hjt/oplsaa/re_1202/nvt-03-1-water-' + str(i) + '.gro', 'r')
    file_4 = open('F:/GMX/gong-hjt/oplsaa/re_1202/nvt-03-1-acn-' + str(i) + '.gro', 'r')

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
            if zz >= (z_max - r_range - r_co):
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
            if zz >= (z_max - r_range - r_co):
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

count_hyd_1 = []
count_hyd_2 = []
count_cyc_1 = []
count_cyc_2 = []
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
            if dd < r_co:
                count += 1


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
            if dd < r_co:
                count += 1
            if count >= 10:
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
            if dd < r_co:
                count += 1
            if count >= 10:
                num_cyc_0 += 1
                if_0 = 1
                break

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
            if dd < r_co:
                count += 1
            if count >= 10:
                num_cyc_1 += 1
                if_1 = 1
                break

        if (if_0 == 0) and (if_1 == 0):
            num_cyc_2 += 1

    print(str(i)+': CYC:  '+str(len(names['cyc_'+str(i)]))+'    '+str(num_cyc_0)+'    '+str(num_cyc_1)+'    '+str(num_cyc_2))

    count_hyd_1 += num_hyd_1
    count_hyd_2 += num_hyd_2

    count_cyc_1 += num_cyc_1
    count_cyc_2 += num_cyc_2


count_hyd_1 /= zhen
count_hyd_2 /= zhen
count_cyc_1 /= zhen
count_cyc_2 /= zhen

print('HYD all: '+str(count_hyd_a)+' '+'in water-'+str(count_hyd_0)+' '+'in ACN-'+str(count_hyd_1)+' '+'other-'+str(count_hyd_2))
print('CYC all: '+str(count_cyc_a)+' '+'in water-'+str(count_cyc_0)+' '+'in ACN-'+str(count_cyc_1)+' '+'other-'+str(count_cyc_2))
''' 
    for line in lines:
        type = line[12:15]
        if type == '  K':
            xx = float(line[21:28])
            yy = float(line[29:36])
            zz = float(line[37:44])
            d_min = 10
            for eoi in EO:
                xxx = float(line[21:28])
                yyy = float(line[29:36])
                zzz = float(line[37:44])
                dx = abs(xxx - xx)
                dy = abs(yyy - yy)
                dz = abs(zzz - zz)
                if dx >= R_box:
                    dx = D_box - dx
                if dy >= R_box:
                    dy = D_box - dy
                if dz >= R_box:
                    dz = D_box - dz

                dd = ((dx ** 2) + (dy ** 2) + (dz ** 2)) ** 0.5

                if dd < d_min:
                    d_min = dd

            k_num = line[15:20]
            kkk.append(k_num)

        if type == ' OW':
            w_num = line[15:20]
            www.append(w_num)

        if type == ' EN':
            n_num = line[15:20]
            nnn.append(n_num)

        if type == 'EO1':
            o_num = line[15:20]
            ooo.append(o_num)

    kkk.sort(key=take_one)

    wrtt.write(' [Kin] \n')
    count = 0
    for j in kkk:
        wrtt.write(j + ' ')
        count += 1
        if count == 12:
            break
    wrtt.write('\n')
    wrtt.write('\n')
    wrtt.write(' [ooo] \n')
    count = 0
    for j in ooo:
        wrtt.write(j + ' ')
        count += 1
        if count == 15:
            wrtt.write('\n')
    wrtt.write('\n')
    wrtt.write('\n')
    wrtt.write(' [nnn] \n')
    count = 0
    for j in nnn:
        wrtt.write(j + ' ')
        count += 1
        if count == 15:
            wrtt.write('\n')
    time.sleep(0.3)
    wrtt.write('\n')
    wrtt.write('\n')
    wrtt.write(' [www] \n')
    count = 0
    for j in www:
        wrtt.write(j + ' ')
        count += 1
        if count == 15:
            wrtt.write('\n')
            count = 0

    wrt_bat.write('gmx rdf -f out'+str(i)+' -n out'+str(i)+' -o out'+str(i)+' -cn outn'+str(i)
                  +' -bin 0.01 -rmax 1 -ref 0 -sel 1 2 3\n')
    time.sleep(1)'''