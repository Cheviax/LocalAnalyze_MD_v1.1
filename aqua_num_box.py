names = locals()

drct = 'H:/GMX_OUT/GONG/NIOOH_TCJ/no_tcj'
name1 = '/sol_'
name2 = '/ion_'

zhen = 50
z1 = 10.1
z2 = 11.6
count = 0

drif = 0.29
aqua_all = 0

count_ion = 0
count_sol = 0

for z in range(zhen):
    #print(z)
    sols = []
    count_ion_i = 0
    count_aqua_i = 0
    aqua_in = []

    red1 = open(drct + name1 + str(z+1) + '.gro', 'r')
    lines1 = red1.readlines()
    del lines1[0]
    del lines1[0]
    del lines1[-1]

    red2 = open(drct + name2 + str(z+1) + '.gro', 'r')
    lines2 = red2.readlines()
    del lines2[0]
    del lines2[0]
    del lines2[-1]

    for line1 in lines1:
        ls_name = line1[12:14]
        ls_5 = line1[21:28]
        ls_6 = line1[29:36]
        ls_7 = line1[37:44]
        ls_num_atom = line1[15:20]
        li_x = float(ls_5)
        li_y = float(ls_6)
        li_z = float(ls_7)

        if ls_name == ' M':
            if (li_z >= float(z1-1)) and (li_z <= z2):
                count_sol += 1
                line_new = ls_5 + ' ' + ls_6 + ' ' + ls_7 + ' ' + ls_num_atom
                sols.append(line_new)

    for line2 in lines2:

        ls_name = line2[13:15]
        ls_5 = line2[21:28]
        ls_6 = line2[29:36]
        ls_7 = line2[37:44]
        li_x = float(ls_5)
        li_y = float(ls_6)
        li_z = float(ls_7)

        if (ls_name == ' H') or (ls_name == ' O'):
            if (li_z >= z1) and (li_z <= z2):
                count_ion_i += 1
                count_ion += 1
                for soli in sols:
                    solis = soli.split()
                    solx = float(solis[0])
                    soly = float(solis[1])
                    solz = float(solis[2])
                    dr2 = (li_x - solx) ** 2 + (li_y - soly) ** 2 + (li_z - solz) ** 2
                    if dr2 <= drif:
                        aqua_in.append(solis[3])

    count_aqua_i = len(set(aqua_in))
    print(count_ion_i)
    aqual = count_aqua_i / count_ion_i
    aqua_all += aqual

aqua_all = aqua_all / zhen

print(aqua_all)



