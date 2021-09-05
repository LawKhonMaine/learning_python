#file = open('./text.txt')

# for line in file:
#     print(line)

# file.seek(0)

#lineslist = file.readlines()

# print(lineslist)

# file.seek(50)

# line100 = file.read(100)

# print(line100)

# file.close()

with open('./text.txt') as file:
    for p in file:
        print(p)

print('other work')
