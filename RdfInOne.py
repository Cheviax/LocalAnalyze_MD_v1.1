import time
names = locals()

zhen = 10

wrt_bat = open('D:/WeChatFiles/WeChat Files/WeChat Files'
                 '/wxid_1z7i8frzi5e412/FileStorage/File/2022-11'
                 '/test/rdfn.one', 'w')

for i in range(100):
    names['l0'+str(i)] = 0
    names['l1'+str(i)] = 0
    names['l2'+str(i)] = 0
    names['l3'+str(i)] = 0

count_zhen = 0

for i in range(zhen):
    count_line = -1
    readd = open('D:/WeChatFiles/WeChat Files/WeChat Files'
                 '/wxid_1z7i8frzi5e412/FileStorage/File/2022-11'
                 '/test/outn' + str(i) + '.xvg', 'r')
    lines = readd.readlines()
    del lines[0:27]

    for line in lines:
        count_line += 1
        print(count_line)
        ls = line.split()
        xx = float(ls[0])
        y1 = float(ls[1])
        y2 = float(ls[2])
        y3 = float(ls[3])
        names['l0' + str(count_line)] += xx
        names['l1' + str(count_line)] += y1
        names['l2' + str(count_line)] += y2
        names['l3' + str(count_line)] += y3

for i in range(100):
    names['l0'+str(i)] /= zhen
    names['l1'+str(i)] /= zhen
    names['l2'+str(i)] /= zhen
    names['l3'+str(i)] /= zhen
    line = str('%.3f'% names['l0'+str(i)])+' '+str('%.5f'% names['l1'+str(i)])\
           +' '+str('%.5f'% names['l2'+str(i)])+' '+str('%.5f'% names['l3'+str(i)])
    wrt_bat.write(line+'\n')
    print(line)

