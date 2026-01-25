#KH 2nd random password generator 

import random

lower = list("abcdefghijklmnopqrstuvwxyz")
upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
num = list("1234567890")
special = list("!@#$%^&*?")

def get_input(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer == "y":
            return True
        if answer == "n":
            return False
        print("Invalid")
        
def get_length(prompt):
    while True:
        length = input(prompt)
        if length.isdigit() and int(length) > 0:
            return int(length)

def make_password(use_lower, use_upper, use_digits, use_special):
    password_requirements = []
    if use_lower:
        password_requirements += lower
    if use_upper:
        password_requirements += upper
    if use_digits:
        password_requirements += num
    if use_special:
        password_requirements += special
    return password_requirements

def make_pool(length, groups, password_requirements):
    password = []
    for g in groups: #make sure at elast one character from each group is chosen
        password.append(random.choice(g))
    #fill the rest
    while len(password) < length:
        password.append(random.choice(password_requirements))

        random.shuffle(password)
        
    return "".join(password)
    
def generate_passwords():
    print("Generate passwords")
    length = get_length("How long do you want the password: ")
    use_lower = get_input("Use Lowercase? (y/n): ")
    use_upper = get_input("Use Uppercase? (y/n): ")
    use_digits = get_input("Use digits? (y/n): ")
    use_special = get_input("Use special characters? (y/n): ")

    groups = []
    if use_lower: groups.append(lower)
    if use_upper: groups.append(upper)
    if use_digits: groups.append(num)
    if use_special: groups.append(special)

    if len(groups) == 0:    
        print("Pick at least one character type please")
        return

    if length < len(groups):
        print("Length is too short for your options")
        return
    password_requirements = make_password(use_lower, use_upper, use_digits, use_special)
    print("Possible passwords:")
    
    for i in range(4):
        print(make_pool(length, groups, password_requirements))

def main():
    print("welcome")

    while True:
        print("1. generate passwords")
        print("2. Exit")

        choice = input("Choice: ").strip()
        if choice == "1":
            generate_passwords()
        elif choice == "2":
            print("goodbye")
            break
        else:
            print("Invalid option")
main()         