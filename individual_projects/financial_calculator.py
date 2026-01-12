#KH second financial calculator

#Function for the Saving times calculator
#Function for compound interest calculator
#Function for Budget Allocator
#Function for Sale price calculator

def savings():
    goal = float(input("What amount are you saving to: $"))
    print("How often will you contribute:\n1. weekly\n2. monthly")
    choice = int(input("choose 1 or 2: "))
    contribution = float(input("How much are you contributing each time: $"))
    if choice == 2:
        months = goal/contribution
        print(f"It will take {months} months to save up ${goal:.2f}")
    elif choice == 1:
        weeks = goal/contribution
        print(f"It will take {weeks} weeks to save up ${goal:.2f}")
    else:
        print("Invalid option")

def compound():
    money = float(input("Starting Amount: $"))
    rate = float(input("Interest Rate percent: "))
    years = int(input("Years spent compounding: "))
    total = money * ((1 + rate / 100) ** years)
    print(f"At the end of {years} you will have a total of ${total:.2f}")



def budget_allocator():
    num_categories = int(input("How many budget categories do you have: "))

    categories = []
    for i in range(num_categories):
        name = input(f"Category {i+1} name:")
        categories.append(name)
    
    income = float(input("What is your monthly income: "))
    percents = []
    for i in range(num_categories):
        percent = float(input(f"What percent is your {categories[i]}: "))
        percents.append(percent)
    def calculate_amount(index):
        return income * (percents[index]/ 100)
        
    for i in range(num_categories):
        amount = calculate_amount(i)
        print(f"{categories[i]} is ${amount:.2f}")




def sale():
    org_num = float(input("How much does the item originally cost:"))
    discount_percentage = float(input("What is the percent of the discount(In decimal form e.g 15% = 0.15):"))
    discount_amount = org_num * discount_percentage
    total = org_num - discount_amount
    print(f"The item now costs ${total:.2f}")
#Function tip calculator
def tip():
    org_num = float(input("How much is the bill:"))
    tip_percentage = float(input("What percent of a tip are you giving(In decimal form e.g 15% = 0.15):"))
    tip_amount = org_num * tip_percentage
    total = tip_amount + org_num
    print(f"The tip amount is ${tip_amount:.2f} and your total is ${total:.2f}")






#Main Function for the user interface
def main():
    print("Enter the number so select an option")
    print("1. Savings Time Calculator")
    print("2. Compound Interest Calculator")
    print("3. Budget Allocator")
    print("4. Sale Price Calculator")
    print("5. Tip Calculator")
    op = input("Enter:")
    if op == "1":
        savings()
    elif op == "2":
        compound()
    elif op == "4":
        sale()
    elif op == "5":
        tip()


main()


