nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map(function,list)


def mapfunction(apple):
    return apple*2


print(list(map(mapfunction, nums)))

# print(list(map(lambda num: num*2, nums)))
