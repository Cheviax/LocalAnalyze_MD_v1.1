#for .gro file

x_or = 1                   # change: 1
y_or = 1                   # change: 1
z_or = 1                   # change: 1

num_add  = 3300
num_r    = 11010
x_change = 0
y_change = 0
z_change = 0
x_set    = 0
y_set    = 0
z_set    = 3

js       = 3
js_r     = 3
sol      = 3
sol_r    = 2573
yes      = 0

with open('gro.txt','r') as f:
    dogs = f.readlines()

for dog in dogs:
    dog_1 = dog[0:15]
    dog_2 = dog[15:]
    doge  = dog_1.split() + dog_2.split()
    out   = ''
    if js     == 3:
        sol   += 1
        js     = 0

    if js_r   == 3:
        sol_r += 1
        js_r   = 0

#dogs.old
    cat_01 = doge[0]
    cat_02 = doge[1]
    cat_03 = doge[2]
    cat_04 = doge[3]
    cat_05 = doge[4]
    cat_06 = doge[5]

# assignment        # residue name
    line_2 = cat_02         # atom
     # atom number
    line_4 = cat_04        # x
    line_5 = cat_05        # y
    line_6 = cat_06        # z

# length of line
    le_2 = len(line_2)

    le_4 = len(line_4)
    le_5 = len(line_5)
    le_6 = len(line_6)

# write
    if yes == 1:
        num_add += 1
        js += 1
        yes = 2

        line_1 = str(sol) + 'SOL'
        le_1 = len(line_1)
        line_3 = str(num_add)
        le_3 = len(line_3)

        k = 0
        while k < 8 - le_1:
            out += ' '
            k = k + 1
        out += line_1
        k = 0
        while k < 7 - le_2:
            out += ' '
            k = k + 1
        out += line_2
        k = 0
        while k < 5 - le_3:
            out += ' '
            k = k + 1
        out += line_3
        k = 0
        while k < 8 - le_4:
            out += ' '
            k = k + 1
        out += line_4
        k = 0
        while k < 8 - le_5:
            out += ' '
            k = k + 1
        out += line_5
        k = 0
        while k < 8 - le_6:
            out += ' '
            k = k + 1
        out += line_6

        with open('water_l.txt', 'a') as f:
            f.write(out)
            f.write('\n')


    elif yes == 2:
        num_add += 1
        js += 1
        yes = 0

        line_1 = str(sol) + 'SOL'
        le_1 = len(line_1)
        line_3 = str(num_add)
        le_3 = len(line_3)

        k = 0
        while k < 8 - le_1:
            out += ' '
            k = k + 1
        out += line_1
        k = 0
        while k < 7 - le_2:
            out += ' '
            k = k + 1
        out += line_2
        k = 0
        while k < 5 - le_3:
            out += ' '
            k = k + 1
        out += line_3
        k = 0
        while k < 8 - le_4:
            out += ' '
            k = k + 1
        out += line_4
        k = 0
        while k < 8 - le_5:
            out += ' '
            k = k + 1
        out += line_5
        k = 0
        while k < 8 - le_6:
            out += ' '
            k = k + 1
        out += line_6

        with open('water_l.txt', 'a') as f:
            f.write(out)
            f.write('\n')



    elif line_2 == 'OW':
        if float(line_4) < 5:
            num_add += 1
            js += 1
            yes = 1

            line_1 = str(sol) + 'SOL'
            le_1 = len(line_1)
            line_3 = str(num_add)
            le_3 = len(line_3)

            k = 0
            while k < 8 - le_1:
                out += ' '
                k = k + 1
            out += line_1
            k = 0
            while k < 7 - le_2:
                out += ' '
                k = k + 1
            out += line_2
            k = 0
            while k < 5 - le_3:
                out += ' '
                k = k + 1
            out += line_3
            k = 0
            while k < 8 - le_4:
                out += ' '
                k = k + 1
            out += line_4
            k = 0
            while k < 8 - le_5:
                out += ' '
                k = k + 1
            out += line_5
            k = 0
            while k < 8 - le_6:
                out += ' '
                k = k + 1
            out += line_6
            with open('water_l.txt', 'a') as f:
                f.write(out)
                f.write('\n')

        else:
            num_r += 1
            js_r += 1

            line_1 = str(sol_r) + 'SOL'
            le_1 = len(line_1)
            line_3 = str(num_r)
            le_3 = len(line_3)

            k = 0
            while k < 8 - le_1:
                out += ' '
                k = k + 1
            out += line_1
            k = 0
            while k < 7 - le_2:
                out += ' '
                k = k + 1
            out += line_2
            k = 0
            while k < 5 - le_3:
                out += ' '
                k = k + 1
            out += line_3
            k = 0
            while k < 8 - le_4:
                out += ' '
                k = k + 1
            out += line_4
            k = 0
            while k < 8 - le_5:
                out += ' '
                k = k + 1
            out += line_5
            k = 0
            while k < 8 - le_6:
                out += ' '
                k = k + 1
            out += line_6
            with open('water_r.txt', 'a') as f:
                f.write(out)
                f.write('\n')


    else :
        num_r += 1
        js_r += 1

        line_1 = str(sol_r) + 'SOL'
        le_1 = len(line_1)
        line_3 = str(num_r)
        le_3 = len(line_3)

        k = 0
        while k < 8 - le_1:
            out += ' '
            k = k + 1
        out += line_1
        k = 0
        while k < 7 - le_2:
            out += ' '
            k = k + 1
        out += line_2
        k = 0
        while k < 5 - le_3:
            out += ' '
            k = k + 1
        out += line_3
        k = 0
        while k < 8 - le_4:
            out += ' '
            k = k + 1
        out += line_4
        k = 0
        while k < 8 - le_5:
            out += ' '
            k = k + 1
        out += line_5
        k = 0
        while k < 8 - le_6:
            out += ' '
            k = k + 1
        out += line_6
        with open('water_r.txt', 'a') as f:
            f.write(out)
            f.write('\n')

print(num_add)