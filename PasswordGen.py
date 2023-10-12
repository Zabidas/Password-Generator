import random

lst = ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c',
       'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*',
       '(', ')', '~', '_', '-', '+', '=', '.', '[', ']', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S',
       'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M')


def generate_password():
    random_item = (random.choice(lst), random.choice(lst), random.choice(lst), random.choice(lst), random.choice(lst),
                   random.choice(lst), random.choice(lst), random.choice(lst), random.choice(lst), random.choice(lst),
                   random.choice(lst), random.choice(lst))
    final = ''.join(random_item)
    return final


a = input("Want a password? y/n: ")
if a == 'y':
    x = 2
    while x > 1:
        print(generate_password())
        x2 = input("One more? y/n: ")
        if x2 == "n":
            x = 1
    else:
        print('bye')
else:
    print('bye')
