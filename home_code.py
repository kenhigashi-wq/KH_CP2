#KH home code

#savings calculator
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