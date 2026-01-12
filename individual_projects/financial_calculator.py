#KH second financial calculator

#function for savings calculator
def savings():
    goal = float(input("What amount are you saving to: $"))#Make input for goal
    print("How often will you contribute:\n1. weekly\n2. monthly")#Ask how often they will input
    choice = int(input("choose 1 or 2: "))#make var for choice
    contribution = float(input("How much are you contributing each time: $"))#How much are they contributing each time?
    if choice == 2:# if there choice is 2
        months = goal/contribution# the months = the goal of money divided by the contribution
        print(f"It will take {months} months to save up ${goal:.2f}")#And the month is how many ti,mes they need to contribute to get to the goal
    elif choice == 1:#if choice is one
        weeks = goal/contribution#do the same thing except the var name is week
        print(f"It will take {weeks} weeks to save up ${goal:.2f}")#same thing
    else:#else
        print("Invalid option")#print invalid
        back_main()

#make a function for the compund stuff
def compound():
    #var for money
    money = float(input("Starting Amount: $"))
    #var for the rate
    rate = float(input("Interest Rate percent: "))
    #ask for the years
    years = int(input("Years spent compounding: "))
    #calculate the total outcome
    total = money * ((1 + rate / 100) ** years)
    #print the outcome
    print(f"At the end of {years} you will have a total of ${total:.2f}")
    back_main()


#make a funciton for the budget allocator
def budget_allocator():
    #ask for how many categories they have
    num_categories = int(input("How many budget categories do you have: "))
    #make a list for the categories
    categories = []
    #loop the stuff d=so they can do it as many times as they want
    for i in range(num_categories):
        #inside of that just print out where they can type the stuff
        name = input(f"Category {i+1} name:")
        #add the input to the list of the category
        categories.append(name)
    #ASK FOR INCOME
    income = float(input("What is your monthly income: "))
    #make a list for the
    percents = []
    #same loop as catgory, just collect the info
    for i in range(num_categories):
        percent = float(input(f"What percent is your {categories[i]}(Make sure they all add up to 100%): "))
        percents.append(percent)
    #inner function!!!!! for calculating
    def calculate_amount(index):
        #Do the calculations and stuff
        return income * (percents[index]/ 100)
    #loop for showing how many moneys they need for each thingies
    for i in range(num_categories):
        amount = calculate_amount(i)
        print(f"{categories[i]} is ${amount:.2f}")
        back_main()



#function for sale
def sale():
    #variables original number
    org_num = float(input("How much does the item originally cost:"))
    #ask for the discount stuff/percentages
    discount_percentage = float(input("What is the percent of the discount(In decimal form e.g 15% = 0.15):"))
    #do the calculation
    discount_amount = org_num * discount_percentage
    total = org_num - discount_amount
    #print the result
    print(f"The item now costs ${total:.2f}")
    back_main()

#Function tip calculator
def tip():
    #ask for the original number
    org_num = float(input("How much is the bill:"))
    #ask for their desired tip percentagge
    tip_percentage = float(input("What percent of a tip are you giving(In decimal form e.g 15% = 0.15):"))
    #do the calculations
    tip_amount = org_num * tip_percentage
    total = tip_amount + org_num
    #print out the results
    print(f"The tip amount is ${tip_amount:.2f} and your total is ${total:.2f}")
    back_main()
#make a function for going back to the funcion so the user can use it forever
def back_main():
    print("Welcome Back!")
    main()
    



#Main Function for the user interface
def main():
    #ask the user what they want to do
    print("Enter the number so select an option")
    print("1. Savings Time Calculator")
    print("2. Compound Interest Calculator")
    print("3. Budget Allocator")
    print("4. Sale Price Calculator")
    print("5. Tip Calculator")
    #make the if stuffs
    op = input("Enter:")
    if op == "1":
        savings()
    elif op == "2":
        compound()
    elif op == "3":
        budget_allocator()
    elif op == "4":
        sale()
    elif op == "5":
        tip()

#call the main function w


main()


