# with open('Lection2/file.txt', 'w') as data:
#     data.write('\nLINE 1\n')
#     data.write('LINE 2\n')

# colors = ['red', 'green', 'blue']
# data = open('Lection2/file.txt', 'a')
# data.writelines(colors)  # разделителей не будет

# data.write('\nLINE 111231\n')
# data.write('LINE 121231\n')
# data.close()

# exit()


path = 'Lection2/file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
exit()
