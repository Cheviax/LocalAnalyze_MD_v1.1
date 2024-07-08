names = locals()
readd = open('D:/WeChatFiles/WeChat Files/WeChat Files/wxid_1z7i8frzi5e412/FileStorage/File/2022-11/dump.xyz', 'r')
read2 = open('D:/WeChatFiles/WeChat Files/WeChat Files/wxid_1z7i8frzi5e412/FileStorage/File/2022-11/dump.txt', 'r')
#   k3      o11     n7      w1

type2name = []

lines = read2.readlines()
for line in lines:
    ls = line.split()
    name = ls[1]
    type2name.append(name)

for i in type2name:
    print(i)

box_xyz = '   10.000   10.000   10.000\n'
lines = readd.readlines()

zhen = 10
line_count = 99122

def take_one(ele):
    return ele[0]

for i in range(zhen):
    print(i)
    atom_number = 0
    line_i = lines[i*line_count:(i+1)*line_count]
    del line_i[0]
    del line_i[0]
    wrt = open('D:/WeChatFiles/WeChat Files/WeChat Files/wxid_1z7i8frzi5e412/FileStorage/File/2022-11/test/out'+str(i)+'.gro', 'w')
    wrt.write('YiGeiWoLiGiaoGiao\n')
    wrt.write('  '+str(line_count-2)+'\n')
    for line in line_i:
        ls          =   line.split()
        atom_type   =   int(ls[0])
        xx          =   float(ls[1])
        yy          =   float(ls[2])
        zz          =   float(ls[3])
        xx_in       =   str('%.3f' % (xx / 10))
        yy_in       =   str('%.3f' % (yy / 10))
        zz_in       =   str('%.3f' % (zz / 10))
        name        =   type2name[atom_type-1]
        atom_number += 1
        number = str(atom_number)
        sps1 = 7-len(name)
        sps2 = 5-len(number)
        sps3 = 8-len(xx_in)
        sps4 = 8-len(yy_in)
        sps5 = 8-len(zz_in)
        line_in = '    1MOL'

        for j in range(sps1):
            line_in += ' '
        line_in += name

        for j in range(sps2):
            line_in += ' '
        line_in += number

        for j in range(sps3):
            line_in += ' '
        line_in += xx_in

        for j in range(sps4):
            line_in += ' '
        line_in += yy_in

        for j in range(sps5):
            line_in += ' '
        line_in += zz_in

        line_in += '\n'

        wrt.write(line_in)
    wrt.write(box_xyz)
        
