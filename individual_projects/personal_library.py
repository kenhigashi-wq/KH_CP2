#KH personal library project

#make a preset book items list or dictionary thing
library_items = [
    {"title": "The Hobbit", "author": "J.R.R Tolkien"},
    {"title": "A Wrinkle in Time", "author": "Madeleine L'Engle"},
    {"title": "Steelheart", "author": "Brandon Sanderson"},
    {"title": "The Chronicles of Narnia: The Horse and His Boy", "author": "C.S. Lewis"},
    {"title": "The Giver", "author": "Lois Lowry"},
    {"title": "Howl's Moving Castle", "author": "Diana Wynne Jones"},
    {"title": "Artemis Fowl", "author": "Eoin Colfer"},
    {"title": "Fablehaven", "author": "Brandon Mull"},
    {"title": "Inkheart", "author": "Cornelia Funke"},
]

#book keys set WORTH 5 POINTS

book_keys = set()

#Make the loop for adding the stuff

for book in library_items:
    key = book["title"].strip().lower() + "|" + book["author"].strip().lower()
    book_keys.add(key)

#make a function for the viewing books
def view():
    #if there is nothign in the library, tell the user that there are no books
    if len(library_items) == 0:
        print("Your library is empty. Use add to insert books")
        return
    #if not, just show them the books
    for book in library_items:
        print(book["title"] + " by " + book["author"])

#make a function for adding books
def add():
    title = input("Title: ").strip()#input for title and author
    author = input("By: ").strip()

    if title == "" or author == "":#if there trying to ragebait you by typing in nothing, tell them
        print("Both title and author are required")
        return 
    #make a variable for the added stuff  
    key = title.lower() + "|" + author.lower()
    #if the stuff is already in your library, tell them
    if key in book_keys:
        print(f"{title} by {author} is already in your library")
        return
    #if everything is fine, add the book
    library_items.append({"title": title, "author": author})
    book_keys.add(key)
    #tell them they added the book and author
    print(f"You have added {title} by {author}")

#make a function for removing items off the library
def remove():
    #same thing, if theres nothing, theres no boos to remove. If theres non tell them
    if len(library_items) == 0:
        print("Your library is empty. There is nothing to remove")
        return
    index = 1#make a variable for the count of keys so the user doesn't have to type out the whole entire thing
    for book in library_items:#print out the options
        print(str(index) + "." + book["title"] + "by" + book["author"])
        index += 1
    #input for the choice
    choice = input("Enter the number of the item you would like to remove: ").strip()
    #If the option isn't a digit, tell them its not a digit, so they have to make it a digit
    if not choice.isdigit():
        print("Invalid. Please enter A NUMBER from the list.")
        return    
    #convert the choice into an integer
    remove = int(choice)
    #Check if it is in the list
    if not (1 <= remove <= len(library_items)):
        print("That number is not in the list")
        return
    #finally, remove the item
    removed = library_items.pop(remove - 1)
    removed_key = removed["title"].strip().lower() + "|" + removed["author"].strip().lower()
    if removed_key in book_keys:
        book_keys.remove(removed_key)
    #report to user
    print("You have removed" + removed["title"] + " by " + removed["author"])

#Make a function for seraching book titles
def search():
    #print their options
    print("What would you like to search by?")
    print("1. Title")
    print("2. Author")
    #get an input
    action = input("Enter one or two: ")
    #if they want to search by title, make a var for option
    if action == "1":
        search = input("What is the Title of the book you want to search: ").strip().lower()
        option = "title"
    #If author, just make the same but for the author path
    elif action == "2":
        search = input("What is the Authors of the book you want to search: ").strip().lower()
        option = "author"
    #anything else is invalid
    else:
        print("Invalid.")
        return
    #if they want to be trolling us, tell em that we have a specialized idiot proof just for them
    if search == "":
        print("You entered nothing.")
        return
    #make a list for matches
    matches = []
    #for the books in the library items, search the stuff
    for book in library_items:
        if search in book[option].lower():
            matches.append(book)
    #if any of the matching is 0, tell them there is no book in existence
    if len(matches) == 0:
        print("No matching found")
        return 
    #if no probelm, show them their searched book
    for book in matches:
        print(book["title"] + " by " + book["author"])

#make the function for main
def main():
    while True:
        #display the stuff
        print("Main menu:")
        print("1. View Items")
        print("2. Add Items")
        print("3. Remove Items")
        print("4. Search Items")
        print("5. Exit")
        choice = input("Choose an action(1-5): ")
        #if the user chooses one, let them view the stuff they want
        if choice == "1":
            view()
        #if the user chooses 2, let them add stuff they want
        elif choice == "2":
            add()
        #if user chooses 3, let them remove stuff they want
        elif choice == "3":
            remove()
        #if user chooese 4, let them search books they want
        elif choice == "4":
            search()
        #if user chooses 5, break the program
        elif choice == "5":
            print("Goodbye. BYeBYeBYe")
            break
        #if anything else is chose, tell them its not available
        else:
            print("Enter a number from 1 to 5")
    
#call the main function to start the thing
main()