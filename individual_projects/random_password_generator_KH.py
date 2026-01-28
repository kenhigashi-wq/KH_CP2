#KH 2nd random password generator 
import random
#Make a list for lower characters
lower = list("abcdefghijklmnopqrstuvwxyz")
#Make a list for upper characters
upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#make a list for numbers 
num = list("1234567890")
#make a list forspecial characters
special = list("!@#$%^&*?")
#function for getting the input so no repititve actions
def get_input(prompt):
    #in a while true loop
    while True:
        #answer equals the prompt of the of the question
        answer = input(prompt).strip().lower()
        #do the routine yes or no and stupid proofing
        if answer == "y":
            return True
        if answer == "n":
            return False
        print("Invalid")
#function for getting the length 
def get_length(prompt):
    #in the while true loop put in the vaiable for length
    while True:
        length = input(prompt)
        #if the length is valid, return
        if length.isdigit() and int(length) > 0:
            return int(length)
#make a function for making the password by basically getting all the stuff added in a list
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
#make a function for making the "pool" for 
def make_pool(length, groups, password_requirements):
    password = []
    for g in groups: #make sure at elast one character from each group is chosen
        password.append(random.choice(g))
    #fill the rest
    while len(password) < length:
        password.append(random.choice(password_requirements))
        #use the random shuffle to randmly get the characters
        random.shuffle(password)
        
    return "".join(password)
 # make a function for generating th e passwords
def generate_passwords():
    print("Generate passwords")
    length = get_length("How long do you want the password: ")#get the input for length calling for the length functoin
    use_lower = get_input("Use Lowercase? (y/n): ")#call the get input functon and ask the questions
    use_upper = get_input("Use Uppercase? (y/n): ")#do the same thing for all variables
    use_digits = get_input("Use digits? (y/n): ")
    use_special = get_input("Use special characters? (y/n): ")
#make a list for groups
    groups = []
    #if using the vaiable, append the list to the groups
    if use_lower: groups.append(lower)
    #do the same for all other variables
    if use_upper: groups.append(upper)
    if use_digits: groups.append(num)
    if use_special: groups.append(special)
#if the length f the group is zero, tell him hes stupdd
    if len(groups) == 0:    
        print("Pick at least one character type please")
        return
#if the length is smaller than the length of groups,
    if length < len(groups):
        #tell them they need more variables
        print("Length is too short for your options")
        return
    #fmake the password requirements again
    password_requirements = make_password(use_lower, use_upper, use_digits, use_special)
    print("Possible passwords:")
    #do it for 4 times., to generate password
    for i in range(4):
        print(make_pool(length, groups, password_requirements))
#make the function for te main menu
def main():
    print("welcome")
    #make the while true loop
    while True:
        #ask to generate or leave
        print("1. generate passwords")
        print("2. Exit")
        #if the choice is 1 call the generate password
        choice = input("Choice: ").strip()
        if choice == "1":
            generate_passwords()
        elif choice == "2":#if not, just break
            print("goodbye")
            break
        #final idiiot proof
        else:
            print("Invalid option")
main()#call main