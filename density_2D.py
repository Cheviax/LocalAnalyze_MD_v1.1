names = locals()

xy_b = 0
z_b = 0
xy_e = 5
z_e = 5

xyz_sl = 100
dxy = (xy_e-xy_b)/xyz_sl
dz  = (z_e-z_b)/xyz_sl

for xyi in range(xyz_sl):
    for zi in range(xyz_sl):
        names['xy_z_num_'+str(xyi)+'_'+str(zi)]=0

solu = ['N1   ',]

for zhen in range(1):
    red = open('nvtt'+str(zhen)+'.gro', 'r')
    lines = red.readlines()
    del lines[-1]
    del lines[-1]
    del lines[0]
    del lines[0]
    for line in lines:
        ls_1 = line[0:5]
        ls_2 = line[5:10]
        ls_3 = line[11:15]
        ls_4 = line[15:20]
        ls_5 = line[21:28]
        ls_6 = line[29:36]
        ls_7 = line[37:44]

        mole_num = str(ls_1)
        mole_nam = ls_2
        atom_nam = ls_3
        atom_num = ls_4
        xx       = float(ls_5)
        yy       = float(ls_6)
        zz       = float(ls_7)

        xyb = xy_b
        zb = z_b

        xy_num = -1
        z_num  = -1
        mass = 0

        if mole_nam in solu:
            for xyii in range(xyz_sl):
                xyb += dxy
                xy_num += 1
                if xx <= xyb:
                    break

            for zii in range(xyz_sl):
                zb += dz
                z_num += 1
                if zz <= zb:
                    break

            if atom_nam == '   C':
                mass = 1
            if atom_nam == '   H':
                mass = 1
            if atom_nam == '   N':
                mass = 1

            names['xy_z_num_'+str(xy_num)+'_'+str(z_num)] += mass

xxyy = -dxy/2
zz = -dz/2

for xyi in range(xyz_sl):
    xxyy += dxy
    zz = -dz / 2
    for zi in range(xyz_sl):
        zz += dz
        names['xy_z_num_'+str(xyi)+'_'+str(zi)] /= 1
        line = str(xxyy)+ ' '+str(zz)+' '+str(names['xy_z_num_'+str(xyi)+'_'+str(zi)])
        print(line)
