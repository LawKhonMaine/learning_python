nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter(function,list)


def even(num):
    return (num % 2) == 0


print(list(filter(even, nums)))
