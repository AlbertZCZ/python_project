
# test = open('name.txt',mode='w')
# test.write('hhhhhh')
# test.close

we = open('name.txt')
for line in we.readlines():
    print(line)