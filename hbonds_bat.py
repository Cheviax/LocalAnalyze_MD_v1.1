drct = 'F:/GMX/gong-hjt/oplsaa/re_1202/test/'
name = 'hbd.bat'
red = open(drct+name, 'w')
sys = '050'
zhen = 10
for i in range(zhen):
    print(i)
    line = 'gmx hbond -f nvt-05-2-water-'+str(i)+'.gro -s nvt-05-2 -n nvt-'\
           + sys +'-water-' + str(i) + '.ndx -num num' + str(i)\
           + ' -dist dist' + str(i) + ' -ang ang' + str(i)
    red.write(line)
    red.write('\n')