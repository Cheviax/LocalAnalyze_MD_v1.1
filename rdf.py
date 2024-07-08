names = locals()
readd = open('D:/WeChatFiles/WeChat Files/WeChat Files/wxid_1z7i8frzi5e412/FileStorage/File/2022-11/dump.xyz', 'r')

#   k3      o11     n7      w1

lines = readd.readlines()

zhen = 10
D_box = 100
R_box = D_box / 2
RDF_max = 10
RDF_dt = 100
count = 0
how_many = 12
per = zhen*how_many

def take_one(ele):
    return ele[0]

for num in range(RDF_dt):
    names['RDF_ddd'+str(num+1)] = (RDF_max/RDF_dt)*(RDF_dt-num-1)
    names['RDF_ooo'+str(num+1)] = 0
    names['RDF_nnn'+str(num+1)] = 0
    names['RDF_www'+str(num+1)] = 0

for i in range(zhen):
    count += 1
    print(count)
    #line_i = lines[0:3]
    line_i = lines[i*99122:(i+1)*99122]
    del line_i[0]
    del line_i[0]
    ooo = []
    nnn = []
    kkk = []
    ooo_count = 0
    nnn_count = 0
    kkk_count = 0

    for j in line_i:
        ls = j.split()
        atom_type = ls[0]
        if (atom_type == '11') or (atom_type == '10'):
            ooo.append(j)
            ooo_count += 1
    #print(ooo_count)

    for j in line_i:
        ls = j.split()
        atom_type = ls[0]
        if atom_type == '7':
            nnn.append(j)
            nnn_count += 1
    #print(nnn_count)

    for j in line_i:
        ls = j.split()
        atom_type = ls[0]
        if atom_type == '3':
            iff = 0
            xk = float(ls[1])
            yk = float(ls[2])
            zk = float(ls[3])
            d_min = 100
            for k in ooo:
                ls = k.split()
                xt = float(ls[1])
                yt = float(ls[2])
                zt = float(ls[3])

                dx = abs(xt-xk)
                dy = abs(yt-yk)
                dz = abs(zt-zk)
                if dx >= R_box:
                    dx = D_box - dx
                if dy >= R_box:
                    dy = D_box - dy
                if dz >= R_box:
                    dz = D_box - dz

                dd = ((dx**2)+(dy**2)+(dz**2))**0.5

                if dd < d_min:
                    d_min = dd

            kk = [d_min, xk, yk, zk]
            kkk.append(kk)

    kkk.sort(key=take_one)
    count_k = 0

    for j in kkk:
        count_k += 1
        xk = j[1]
        yk = j[2]
        zk = j[3]
        for k in ooo:
            ls = k.split()
            xt = float(ls[1])
            yt = float(ls[2])
            zt = float(ls[3])

            dx = abs(xt - xk)
            dy = abs(yt - yk)
            dz = abs(zt - zk)
            if dx >= R_box:
                dx = D_box - dx
            if dy >= R_box:
                dy = D_box - dy
            if dz >= R_box:
                dz = D_box - dz

            dd = ((dx ** 2) + (dy ** 2) + (dz ** 2)) ** 0.5

            if dd < RDF_max:
                for l in range(RDF_dt):
                    if dd > names['RDF_ddd' + str(l + 1)]:
                        names['RDF_ooo' + str(l + 1)] += 1
                        break

        for k in nnn:
            ls = k.split()
            xt = float(ls[1])
            yt = float(ls[2])
            zt = float(ls[3])

            dx = abs(xt - xk)
            dy = abs(yt - yk)
            dz = abs(zt - zk)
            if dx >= R_box:
                dx = D_box - dx
            if dy >= R_box:
                dy = D_box - dy
            if dz >= R_box:
                dz = D_box - dz

            dd = ((dx ** 2) + (dy ** 2) + (dz ** 2)) ** 0.5

            if dd < RDF_max:
                for l in range(RDF_dt):
                    if dd > names['RDF_ddd' + str(l + 1)]:
                        names['RDF_nnn' + str(l + 1)] += 1
                        break

        for k in line_i:
            ls = k.split()
            atom_type = ls[0]
            if atom_type == '1':
                xt = float(ls[1])
                yt = float(ls[2])
                zt = float(ls[3])

                dx = abs(xt - xk)
                dy = abs(yt - yk)
                dz = abs(zt - zk)
                if dx >= R_box:
                    dx = D_box - dx
                if dy >= R_box:
                    dy = D_box - dy
                if dz >= R_box:
                    dz = D_box - dz

                dd = ((dx ** 2) + (dy ** 2) + (dz ** 2)) ** 0.5

                if dd < RDF_max:
                    for l in range(RDF_dt):
                        if dd > names['RDF_ddd' + str(l + 1)]:
                            names['RDF_www' + str(l + 1)] += 1
                            break

        if count_k == how_many:
            print(count_k)
            break

for num in range(RDF_dt):
    line = str(names['RDF_ddd' + str(num + 1)]+0.5*RDF_max/RDF_dt)+' '\
           +str(names['RDF_ooo' + str(num + 1)]/per)+' '\
           +str(names['RDF_nnn' + str(num + 1)]/per)+' '\
           +str(names['RDF_www' + str(num + 1)]/per)

    print(line)





