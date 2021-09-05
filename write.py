# with open('./about.txt', 'w') as file:
#     file.write("Hello,my name is law khon maine.")


# # other work

# with open('./about.txt', 'a') as file:
#     file.write("\nI am 18 years old.")


# lists = ["Hello,my name is law khon maine.", "\nI am 18 years old."]

# with open('./about.txt', 'w') as file:
#     file.writelines(lists)


users = [input('Your name :'), "\n", input('Your age :'), "\n",
         input('Your sex :')]

with open("./about.txt", 'w') as file:
    file.writelines(users)
