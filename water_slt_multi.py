drct = 'H:/GMX_OUT/JIANG/CO2_NEW/none/00/'

ndx = 'idx.ndx'
zhen = 1000

for i in range(zhen):
    print(i)
    name = drct+'gro_'+str(i+3000)+'.gro'
    name2 = drct+'idx_'+str(i+3000)+'.ndx'
    read = open(name, 'r')
    lines = read.readlines()

    rat = open(name2, 'w')

    del lines[0]
    del lines[0]
    del lines[-1]

    rat.write('[ sol_slt ]')
    rat.write('\n')

    iff = 0
    count = 0

    for line in lines:
        ls_1 = line[0:5]
        ls_2 = line[5:10]
        ls_3 = line[11:15]
        ls_4 = line[15:20]
        ls_5 = line[21:28]
        ls_6 = line[29:36]
        ls_7 = line[37:44]
        if float(ls_7) <= 1.91:
            iff = 1
            rat.write(ls_4)
            rat.write(' ')
            count += 1

        if count == 15:
            count = 0
            rat.write('\n')

    rat.write('\n')