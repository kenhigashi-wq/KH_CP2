#KH 2nd Simple morse code translator
#make a tuple for endligh charcters
english = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
           "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
             "u", "v", "w", "x", "y", "z")
#make a tuple for morse code
morse = ( 
".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
    "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
    "..-","...-",".--","-..-","-.--","--.."
)

#making english, into moress code function
def eng_to_morse(text):
    #make a variable for results
    result = ""
    #make a for loop
    for char in text.lower():
        # if the character is in english, add the morse code that matches with the index of the english
        if char in english:
            result += morse[english.index(char)] + " "
        #if the charatcer is space, replace with /
        elif char == " ":
            result += "/ "
        else:
            continue
    return result.strip()
#make a function for morse code to english
def morse_to_eng(code):
    #make a variable for results
    result = ""
    #make a variable for letters
    letters = code.strip().split()
    #iteraze for if the symbol is in letters, add the english that matches with the index of the morse
    for symbol in letters:
        if symbol == "/":
            result += " "
            continue
        if symbol in morse:
            result += english[morse.index(symbol)]
        else:
            continue
    return result

#make the main function
def main():
    #print out a welcom thing
    print("Welcome to translator for morse code")
    #mae a loop
    while True:
        print("1. Translate from morse code to english")
        print("2. Translate from English to morse code")
        print("3. Exit")
        #give them the options and let them decide
        choice = input("Coose an option(1-3): ")
        #if choice = 1, call the function for morse code to english translator
        if choice == "1":
            #ask them what to translate
            code = input("What is the code you want to ttranslate? ")
            #do the parameter thing, I think it was called, calling the parameter
            print("Your code says: ")
            print(morse_to_eng(code))
        # if the choice is 2, just do the same thing for the 
        elif choice == "2":
            text = input("What is the message you need in morse code? ")
            print("Your message says:")
            print(eng_to_morse(text))
        #if they wan to exit, just break
        elif choice == "3":
            print("bye")
            break
        else:
            print("Invalid, try again")
#run the program
main()