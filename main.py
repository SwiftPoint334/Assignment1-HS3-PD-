"""
Copyright - 2022 Parker Doggett
"""

# Name question/answer
user_name = input("Hello, what is your name?")
print(f"Welcome, {user_name}!\nThis program was created by Parker Doggett.\n")

# Weapon Question
print("You are in the woods, you've just woken up...")
weapon = input("A pistol, an axe, and a shovel lie before you.\nSelect a weapon (enter: gun, axe or shovel): ")
print(f"The {weapon}... great choice.\n")

progress = "{:.0%}".format(1/3)
print(f"You are {progress} done!\n\n")

# Friend question
num_friends = int(input("You arrive in your hometown.\nYou are given an option of how many friends to bring, how many would you like to bring?(Must be a whole number): "))
print(f"You have chosen to bring {num_friends}, so including you, you have {num_friends + 1} in your group.\n")

progress = "{:.0%}".format(2/3)
print(f"You are {progress} done!\n\n")

# Box question
select_box = input("You enter the woods again. Three colored boxes lie before you.\n What box would you like to choose?(Enter: red, blue, or green.): ")
print(f"You have chosen the {select_box} box.")

progress = "{:.0%}".format(3/3)
print(f"You are {progress} done!\n\n")

# Summary
print("Thank you for playing! Below is a summary of what you chose on your adventure.")
print(f"Your weapon: {weapon}\nHow many friends you brought: {num_friends}\nWhat color box you chose: {select_box}.")
print("The end!")