drct = 'F:/GMX/gong-hjt/oplsaa/re_1202/test/'

zhen = 10
num_all = 0
for i in range(zhen):
    red = open(drct+'num'+str(i)+'.xvg', 'r')
    lines = red.readlines()
    line = lines[-1]
    ls = line.split()
    num = int(ls[1])
    print(str(i)+'  '+str(num))
    num_all += num

num_all = num_all / zhen
print(num_all)