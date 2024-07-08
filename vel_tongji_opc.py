names = locals()

z_b = 17
z_e = 20
x_b = 2.39
x_e = 3.79

for i in range(100):
    names['vel_list_'+str(i+1)] = float(0)
    names['vel_num_'+str(i+1)] = 0
    names['vel_max_'+str(i+1)] = 0
    names['vel_min_'+str(i+1)] = 0
    names['x_if_'+str(i+1)] = x_b + (x_e-x_b)/100*(i+1)
    names['v_a_'+str(i+1)] = 0

zhen = 1000

for j in range(zhen):
    print(j)
    red = open('H:/GMX_OUT/mo/un_push/push1/sol'+(str(j+0))+'.gro', 'r')
    lines = red.readlines()
    del lines[0]
    del lines[0]
    del lines[-1]
    del lines[-1]
    for line in lines:
        ls_1 = line[0:5]
        ls_2 = line[5:10]
        ls_3 = line[11:15]
        ls_4 = line[15:20]
        ls_5 = line[21:28]
        ls_6 = line[29:36]
        ls_7 = line[37:44]
        ls_x = line[61:69]
        xx = float(ls_5)
        zz = float(ls_7)
        vz = float(ls_x)
        if ls_3 == '  OW':
            if (zz >= z_b) and (zz <= z_e):
                #  print('ok')
                for i in range(100):
                    if xx <= names['x_if_' + str(i + 1)]:
                        names['vel_num_' + str(i + 1)] += 1
                        names['vel_list_' + str(i + 1)] += vz
                        break

    for i in range(100):
        if names['vel_num_' + str(i + 1)] == 0:
            names['vel_num_' + str(i + 1)] = 1
        # print(names['vel_num_'+str(i+1)])
        names['vel_list_' + str(i + 1)] = names['vel_list_' + str(i + 1)] / names['vel_num_' + str(i + 1)]
        names['v_a_'+str(i+1)] += names['vel_list_' + str(i + 1)]
        names['vel_num_'+str(i+1)] = 0
        names['vel_list_'+str(i+1)] = 0

print('ok')
for i in range(100):
    names['v_a_' + str(i + 1)] = names['v_a_' + str(i + 1)] / zhen
    linenew = str(names['x_if_'+str(i+1)])+' '+str(names['v_a_' + str(i + 1)])
    print(linenew)


