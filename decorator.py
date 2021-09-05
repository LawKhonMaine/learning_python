#example(1)

# def greet(fun):

#     def wrapper(name):
#         # before
#         print("Hello")
#         fun(name)
#         # after
#         print('Good bye')

#     return wrapper


# @greet
# def sayName(name):
#     print(name)

# sayName("law khon maine")


#example(2)

def greet(user):

    def before():
        print('Welcome from here!')
        user()
        print('Nice to meet you.')

    return before


@greet
def userName():
    name = input('Write your name :')
    print(f'Hello {name}')


userName()


#example(3)
