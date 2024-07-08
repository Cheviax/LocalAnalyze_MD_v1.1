red = open('gro_1.txt', 'r')
wrt = open('gro_re.txt', 'w')

lines = red.readlines()

mole_num_from    = 730
atom_num_from   = 2564
iff = 0

count_per = 3
count = 0
atom_num        = atom_num_from

for line in lines:
    ls_1 = line[0:5]
    ls_2 = line[5:10]
    ls_3 = line[11:15]
    ls_4 = line[15:20]
    ls_5 = line[21:28]
    ls_6 = line[29:36]
    ls_7 = line[37:44]
    count += 1

    if count == 1:

        if (float(ls_7) >= 0.51) and (float(ls_7) <= 10.51) :
            iff = 1
            mole_num_from += 1

        else:
            iff = 0

    if count == count_per:
        count = 0

    if iff == 1:
        atom_num_from += 1
        li_1 = str(mole_num_from)
        li_2 = ls_2.strip()
        li_3 = ls_3.strip()
        li_4 = str(atom_num_from)
        li_5 = str('%.3f' % (float(ls_5)))
        li_6 = str('%.3f' % (float(ls_6)))
        li_7 = str('%.3f' % (float(ls_7)))

        name_a = ''

        spc1 = 5 - len(li_1)
        spc2 = 10 - len(li_2 + li_3)
        spc3 = 5 - len(li_4)
        spc4 = 8 - len(li_5)
        spc5 = 8 - len(li_6)
        spc6 = 8 - len(li_7)

        line_new = ''
        for i in range(spc1):
            line_new += ' '
        line_new += li_1
        line_new += li_2
        for i in range(spc2):
            line_new += ' '
        line_new += li_3
        for i in range(spc3):
            line_new += ' '
        line_new += li_4
        for i in range(spc4):
            line_new += ' '
        line_new += li_5
        for i in range(spc5):
            line_new += ' '
        line_new += li_6
        for i in range(spc6):
            line_new += ' '
        line_new += li_7

        line_new += name_a
        print(line_new)
        wrt.write(line_new)
        wrt.write('\n')

