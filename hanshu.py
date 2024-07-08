import math


def water_angle(O,M):

    x1 = O[0]
    y1 = O[1]
    z1 = O[2]

    x2 = M[0]
    y2 = M[1]
    z2 = M[2]

    dx = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5
    dz = (z1 - z2)

    if dx != 0:
        tant = dz / dx
    else:
        tant = 1000
    return tant


def msd_xyz(xb, yb, zb, xe, ye, ze, bx2, by2, bz2):
    dx = abs(xe-xb)
    dy = abs(ye-yb)
    dz = abs(ze-zb)
    if dx > bx2:
        dx = 2*bx2-dx
    if dy > by2:
        dy = 2*by2-dy
    if dz > bz2:
        dz = 2*bz2-dz

    dd = dx**2 + dy**2 + dz**2
    return dd

def sel_xyz(IN, x_min, x_max, y_min, y_max, z_min, z_max, name):
    NUM = []
    XXX = []
    YYY = []
    ZZZ = []
    for ini in IN:
        if ini[11:15] == name:
            zi = float(ini[37:44])
            if zi >= z_min:
                if zi <= z_max:
                    yi = float(ini[2:3])
                    if yi >= y_min:
                        if yi <= y_max:
                            xi = float(ini[3:4])
                            if xi >= x_min:
                                if xi <= x_max:
                                    NUM.append(int(ini[0:5]))
                                    XXX.append(float(ini[21:28]))
                                    YYY.append(float(ini[29:36]))
                                    ZZZ.append(float(ini[37:44]))

    return NUM, XXX, YYY, ZZZ

def sel_d(IN, CO, D_in, name):
    NUM = []
    XXX = []
    YYY = []
    ZZZ = []
    for ini in IN:
        if ini[11:15] == name:
            xi = float(ini[21:28])
            yi = float(ini[29:36])
            zi = float(ini[37:44])
            for coi in CO:
                xc = coi[0]
                yc = coi[1]
                zc = coi[2]
                dd = (xc - xi) ** 2 + (yc - yi) ** 2 + (zc - zi) ** 2
                if dd <= (D_in ** 2):
                    NUM.append(int(ini[0:5]))
                    XXX.append(float(ini[21:28]))
                    YYY.append(float(ini[29:36]))
                    ZZZ.append(float(ini[37:44]))
                    break

    return NUM, XXX, YYY, ZZZ

def sel_z(IN, z_min, z_max, name):
    NUM = []
    XXX = []
    YYY = []
    ZZZ = []
    for ini in IN:
        zi = float(ini[37:44])
        if zi >= z_min:
            if zi <= z_max:
                if ini[11:15] == name:
                    NUM.append(int(ini[0:5]))
                    XXX.append(float(ini[21:28]))
                    YYY.append(float(ini[29:36]))
                    ZZZ.append(float(ini[37:44]))

    return NUM, XXX, YYY, ZZZ


def sel_num(IN, NUM_IN):
    XXX = []
    YYY = []
    ZZZ = []
    for ini in IN:
        numi = int(ini[0:5])
        if numi in NUM_IN:
            XXX.append(float(ini[21:28]))
            YYY.append(float(ini[29:36]))
            ZZZ.append(float(ini[37:44]))
    return XXX, YYY, ZZZ

'''
name = '  OW'
z_min = 0
z_max = 5
tryy = open('H:\GMX_OUT\GONG\done\_final\ertry_0922\gro_2.gro', 'r')
lines = tryy.readlines()
del lines[0]
del lines[0]
del lines[-1]
num = sel_z(lines, z_min, z_max, name)[0]
zzz = sel_z(lines, z_min, z_max, name)[1]
print(num)
print(zzz)
'''

'''
m = [0,0,0]
o = [0,1,-1]
ang = water_angle(o,m)
ang = math.atan(ang)
ang = ang / math.pi * 180
print(ang)
'''