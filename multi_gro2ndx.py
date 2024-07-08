import time
zhen = 10
R_box = 5
D_box = 10

def take_one(ele):
    return ele[0]

wrt_bat = open('D:/WeChatFiles/WeChat Files/WeChat Files'
                 '/wxid_1z7i8frzi5e412/FileStorage/File/2022-11'
                 '/test/run.bat', 'w')

for i in range(zhen):
    readd = open('D:/WeChatFiles/WeChat Files/WeChat Files'
                 '/wxid_1z7i8frzi5e412/FileStorage/File/2022-11'
                 '/test/out' + str(i) + '.gro', 'r')
    wrtt = open('D:/WeChatFiles/WeChat Files/WeChat Files'
                 '/wxid_1z7i8frzi5e412/FileStorage/File/2022-11'
                 '/test/out' + str(i) + '.ndx', 'w')
    lines = readd.readlines()
    del lines[0]
    del lines[0]
    del lines[-1]
    EO = []
    kkk = []
    ooo = []
    nnn = []
    www = []

    for line in lines:
        type = line[12:15]
        if type == 'EO1':
            xx = float(line[21:28])
            yy = float(line[29:36])
            zz = float(line[37:44])
            eoi = [xx, yy, zz]
            EO.append(eoi)

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
    time.sleep(1)