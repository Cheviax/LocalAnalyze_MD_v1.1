red = open('gro_1.txt', 'r')
wrt = open('gro_re.txt', 'w')

lines = red.readlines()

mole_num_add    = 1
atom_num_from   = 3909
x_add           = 0.962
y_add           = 0.842
z_add           = 1.317

atom_num        = atom_num_from
mole = 2
orr = 0

x_box = 9.696
y_box = 8.4

x_multi = 14
y_multi = 12

x_plus = x_box / x_multi
y_lpus = y_box / y_multi

x_set = x_plus * -0.5
y_set = y_lpus * -0.5

for i in range(x_multi):
    x_set += x_plus
    y_set = y_lpus * -0.5
    for j in range(y_multi):
        y_set += y_lpus

        iff = 1

        if (x_set > 3.2) and (x_set < 6.48):
            if (y_set > 2.57) and (y_set < 5.83):
                iff = 0

        if iff == 1:
            mole += 1
            for line in lines:
                atom_num += 1
                orr += 1

                ls_1 = line[0:5]
                ls_2 = line[5:10]
                ls_3 = line[11:15]
                ls_4 = line[15:20]
                ls_5 = line[21:28]
                ls_6 = line[29:36]
                ls_7 = line[37:44]

                li_1 = str(mole)
                li_2 = ls_2.strip()
                li_3 = ls_3.strip()
                li_4 = str(atom_num)
                li_5 = str('%.3f' % (float(ls_5) + x_add + x_set))
                li_6 = str('%.3f' % (float(ls_6) + y_add + y_set))
                li_7 = str('%.3f' % (float(ls_7) + z_add))

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






