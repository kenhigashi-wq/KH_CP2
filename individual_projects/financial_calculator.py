#KH second financial calculator

#Function for the Saving times calculator
#Function for compound interest calculator
#Function for Budget Allocator
#Function for Sale price calculator






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
    if op == "4":
        sale()
    elif op == "5":
        tip()


main()


