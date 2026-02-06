#KH 2nd Movie reccomender
import csv

try:
    with open("individual_projects\Movies list - Sheet1.csv", "r") as file:
        content = []
        for line in file:
            content.append(line.strip())
    print(content)
except:
    print("File not found.")
else:
    for line in content:
        print(f"{line}")

#test
 
try:
    with open("individual_projects\movies.csv", mode = "r", newline = '') as sample:
        reader = csv.reader(sample)
        header = next(reader)
        users = []
        for line in reader:
            users.append(
                {
                    header[0]: line[0],
                    header[1]: line[1],
                }
            )
except:
    print("File not found.")
else:
    for user in users:
        print(user)

def main():
    while True:
        print("Type the number for the action you would like to perform")
        print("1. Search / Get Recommendations")
        print("2. Print Full Movie List")
        print("3. Exit")
        choice = input("choice: ")
        if choice == "1":
            print("Choose filters to apply (enter numbers separated by commas, e.g., 1,3):")
            print("1.Genre" \
            "2.Director" \
            "3.Actor" \
            "4.Length (min/max)")
        filter = input("Fliters:")

main()











