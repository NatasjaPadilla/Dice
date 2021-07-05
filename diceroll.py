import random


def roll():
    x = random.randint(1, 6)
    if x == 1:
        print(".")
    elif x == 2:
        print(":")
    elif x == 3:
        print(":.")
    elif x == 4:
        print("::")
    elif x == 5:
        print(":.:")
    else:
        print(":::")


while True:
    ans = input("would you like to roll the die? y/n: ")
    if ans.lower() == "y":
        roll()
    else:
        print("ok")
        break

