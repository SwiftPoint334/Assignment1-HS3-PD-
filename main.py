"""
Copyright - 2022 Parker Doggett
"""

# money system
money = 10

# Name question/answer
user_name = input("Hello, what is your name?")
print(f"Welcome, {user_name}!\nThis program was created by Parker Doggett.\n")
print(f"Your current balance is ${money}.\n")

# Weapon Question
print("You are in the woods, you've just woken up...")
weapon = input("A pistol, an axe, and a shovel lie before you.\nSelect a weapon (enter: gun, axe or shovel): ")
print(f"The {weapon}... great choice.\n")

progress = "{:.0%}".format(1/3)
print(f"You are {progress} done!\n\n")

# Enemy Question
enemy = input("You hear a noise in the distance, what do you do?\n1. Run\n2. Hide\n3. Attack\nEnter 1, 2, or 3: ")
if enemy == "1":
    if weapon == "gun":
        print("You run away, but the enemy catches up to you, so you shoot it.")
        money = money + 5
        print(f"You now have ${money}.\n")
    if weapon == "axe":
        print("You run away, but the enemy catches up to you, so you hit it with the axe. The enemy stops the axe with its hand, and kills you. You lose.")
        exit()
    if weapon == "shovel":
        print("You run away, but the enemy catches up to you, so you hit it with the shovel. The enemy stops the shovel with its hand, and kills you. You lose.")
        exit()
elif enemy == "2":
    print("You hide, but the enemy finds you. You are dead.")
    pay = input("Would you like to pay $5 to continue? (y/n): ")
    if pay == "y":
        if money < 5:
            print("You do not have enough money.")
            exit()
        else:
            money = money - 5
            print(f"Your new balance is ${money}.")
    elif pay == "n":
        print("You are dead.")
        exit()
elif enemy == "3":
    if weapon == "gun":
        print("You shoot the enemy, and it dies.")
        money = money + 5
        print(f"You now have ${money}.\n")
    if weapon == "axe":
        print("You hit the enemy with the axe, and it dies.")
        money = money + 5
        print(f"You now have ${money}.\n")
    if weapon == "shovel":
        print("You hit the enemy with the shovel, and it dies.")
        money = money + 5
        print(f"You now have ${money}.\n")

# Friend question
num_friends = int(input("You arrive in your hometown.\nYou are given an option of how many friends to bring, how many would you like to bring?(Must be a whole number): "))
print(f"You have chosen to bring {num_friends}, so including you, you have {num_friends + 1} in your group.\n")

progress = "{:.0%}".format(2/3)
print(f"You are {progress} done!\n\n")

# Box question
select_box = input("You enter the woods again. Three colored boxes lie before you.\n What box would you like to choose?(Enter: red, blue, or green.): ")
print(f"You have chosen the {select_box} box.")

# Poison Box Question
if select_box == "red":
    print("You have chosen the red box. You are dead.")
    exit()
elif select_box == "blue":
    if num_friends >= 2:
        print("Your friends have saved you from the poison hidden in the blue box.")
    else:
        print("The box contained hidden poison. You are dead.")
        exit()
elif select_box == "green":
    print("The box contained a key. You are free.")
    exit()

progress = "{:.0%}".format(3/3)
print(f"You are {progress} done!\n\n")

# Summary
print("Thank you for playing! Below is a summary of what you chose on your adventure.")
print(f"Your weapon: {weapon}\nHow many friends you brought: {num_friends}\nWhat color box you chose: {select_box}.")
print(f"Your final balance is ${money}.")
print("The end!")