names = locals()

drct = 'F:/GMX/gong-hjt/oplsaa/re_1202/test/'
zhen = 10

z_min   =   9.51
z_max   =   10.51
r_range =   1

water_point     =   3
for i in range(zhen):
    names['sol_'+str(i)] = []

sys = '050'

for i in range(zhen):
    file_1 = open(drct + 'nvt-'+sys+'-water-' + str(i) + '.gro', 'r')

    lines = file_1.readlines()
    del lines[0]
    del lines[0]
    del lines[-1]
    line_count = 0
    iff = 0
    num_count = []
    for line in lines:
        line_count += 1
        if line_count == 1:
            zz = float(line[37:44])
            if zz >= (z_max - r_range):
                iff = 1
                atom_num = int(line[15:20])
                print(atom_num)
                num_count.append(atom_num)

            else:
                iff = 0

        else:
            if iff == 1:
                zz = float(line[37:44])
                atom_num = int(line[15:20])
                num_count.append(atom_num)

        if line_count == water_point:
            line_count = 0


    file_2 = open(drct + 'nvt-'+sys+'-water-' + str(i) + '.ndx', 'w')
    file_2.write('[water at surface]\n')
    co = 0
    for i in num_count:
        co += 1
        file_2.write(str(i))
        file_2.write(' ')
        if co == 15:
            file_2.write('\n')
            co = 0