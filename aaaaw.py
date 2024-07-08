#for .gro file

x_or = 1                   # change: 1
y_or = 1                   # change: 1
z_or = 1                   # change: 1

num_add  = 2400
x_change = 0
y_change = 0
z_change = 0
x_set    = 0
y_set    = 0
z_set    = 3

with open('gro.txt','r') as f:
    dogs = f.readlines()

for dog in dogs:
    dog_1 = dog[0:14]
    dog_2 = dog[15:]
    doge  = dog_1.split() + dog_2.split()
    out   = ''
    num_add += 1
    print(doge)

