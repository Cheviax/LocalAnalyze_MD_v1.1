names = locals()

for i in range(87):
    ii = 16 + i * 2
    io = 17 + i * 2
  #  print(ii)
 #   print(io)
    print('echo ' + str(ii) + ' ' + str(ii) + ' | '
          + 'gmx hbond -f nvtt.gro -n nvtt.ndx -s nvt.tpr -num hbd_' + str(i + 2) + 'i')
    print('echo ' + str(ii) + ' ' + str(io) + ' | '
          + 'gmx hbond -f nvtt.gro -n nvtt.ndx -s nvt.tpr -num hbd_' + str(i + 2) + 'o')

'''
 echo 100 100 | gmx hbond -f nvtt.gro -n nvtt.ndx -s nvt.tpr -num try_h_11
'''
for i in range(87):
    r_i = open('hbd_' + str(i+2) + 'i.xvg'.'r')
    r_o = open('hbd_' + str(i+2) + 'o.xvg','r')
    lines_i = r_i.readlines()
    lines_o = r_o.readlines()
    line_i  = lines_i[25]
    line_o  = lines_o[25]
    i_sp    = line_i.split()
    o_sp    = line_o.split()

    naems['hbd_i_' + str(i+2)] = i_sp[2]
    names['hbd_o_' + str(i+2)] = o_sp[2]

    print(naems['hbd_i_' + str(i+2)] + naems['hbd_o_' + str(i+2)])
