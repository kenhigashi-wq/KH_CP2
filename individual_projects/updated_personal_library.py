#KH personal library project
import csv
#Make the four meaningful fields and make some variables
fields = ["title", "creator", "year", "genre"]
library = []
dirty = False
file_name = ""

#Make the loading and saving functions first
def load_library():
    library.clear()
    try:
        with open(file_name, "r", newline="") as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader, start = 2):
                title = row.get("title", "").strip()
                creator = row.get("creator", "").strip()
                year = row.get("year", "").strip()
                genre = row.get("genre", "").strip()

                if (not title) or (not creator) or (not year.isdigit()) or (not (1 <= len(year) <= 4)) or (not genre):
                    print(f"Warning: skipping bad row at line {i}")
                    continue

                library.append({
                    "title": title,
                    "creator": creator,
                    "year": year,
                    "genre": genre
                })
    except FileNotFoundError:
        #create an empty file with header
        with open(file_name, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames = fields)
            writer.writeheader()

#Function for saving the library
def save_library():
    with open(file_name, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(library)
    print("Library has been saved succesfully")

#make a function for the viewing books
def view_simple():
    #if there is nothign in the library, tell the user that there are no books
    if not library:
        print("Your library is empty. Use add to insert books")
        return
    #if not, just show them the books
    for i, item in enumerate(library, start=1):
        print(f"{i}. {item['title']} - {item['creator']}")

def view_detailed():
 #if there is nothign in the library, tell the user that there are no books
    if not library:
        print("Your library is empty. Use add to insert books")
        return
    #if not, just show them the books
    for i, item in enumerate(library, start=1):
        print(f"\n[{i}]")
        print("Title: ", item["title"])
        print("Creator: ", item["creator"])
        print("Year: ", item["year"])
        print("Genre: ", item["genre"])
    print()

#A function for basically checking the years and stuff
def prompt_year(default = None):
    while True:
        if default is None:
            y = input("Year (digits): ").strip()        
        else:
            y = input(f"Year (digits) [{default}]: ").strip() or default
        #idiot proof for the years
        if y.isdigit() and 1 <= len(y) <= 4:
            return y
        print("Invalid year, use 1-4 digits and try again")


#make a function for adding books
def add_item():
    global dirty
    title = input("Title: ").strip()#input for title and author
    creator = input("By: ").strip()#input for the creator
    year = prompt_year()#input for the year thing
    genre = input("Genre: ").strip()#input for the genre
    if not title or not creator or not genre:#if there trying to ragebait you by typing in nothing, tell them
        print("Title, creator, and genre are required")
        return
    library.append({"title": title, "creator": creator, "year": year, "genre": genre})
    dirty = True
    print("Item added")

#Function for updating item
def update_item():
    global dirty
    view_simple()#Call the simple view
    choice = input("Update which number: ").strip()#ask which one they want to update
    if not choice.isdigit() or not (1 <= int(choice) <= len(library)):#idiot proof once more
        print("Invalid")
        return
    index = int(choice) - 1#make a variable for the real index
    item = library[index]
    new_title = input(f"Title [{item['title']}]: ").strip() or item["title"]
    new_creator = input(f"Creator [{item['creator']}]: ").strip() or item["creator"]
    new_year = prompt_year(item["year"])
    new_genre = input(f"Genre [{item['genre']}]: ").strip() or item["genre"]
    item.update(title = new_title, creator = new_creator, year = new_year, genre = new_genre)
    dirty = True
    print("Succesfully Updated")


#make a function for removing items off the library
def delete_item():
    global dirty
    #call the viewing simple
    view_simple()
    #ask for which one to delete
    choice = input("Delete which number: ").strip()
    #Idiot proof for the if digit or nah
    if not choice.isdigit() or not (1 <= int(choice) <= len(library)):
        print("Invalid")
        return
    removed = library.pop(int(choice) - 1)
    print(f"Deleted {removed['title']} - {removed['creator']}")
    dirty = True

#Start the program

def main():
    global file_name, dirty

    file_name =  input(f"Enter your data file path: ").strip() or "library.csv"
    load_library()

    while True:
        print("\nMenu:")
        print("1. Show simple list")
        print("2. Show detailed list")
        print("3. Add item")
        print("4. Update item")
        print("5. Delete item")
        print("6. Save")
        print("7. Reload")
        print("8 Exit")

        c = input("Choose from 1 to 8: ").strip()

        if c == "1":
            view_simple()
        elif c == "2":
            view_detailed()
        elif c == "3":
            add_item()
        elif c == "4":
            update_item()
        elif c == "5":
            delete_item()
        elif c == "6":
            save_library()
            dirty = False
        elif c == "7":
            if dirty and input("Unsaved, reload anyway?(y/n)") != "y":
                continue
            load_library(); dirty = False
            print("Reloaded")
        elif c == "8":
            if dirty and input("Save before exit?(y/n)") == "y":
                save_library()
            print("BYYYYYE")
            break
        else:
            print("Invalid")

main()