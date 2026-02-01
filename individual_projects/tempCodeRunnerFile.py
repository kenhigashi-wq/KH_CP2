#KH 2nd Simple morse code translator

english = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
           "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
             "u", "v", "w", "x", "y", "z")

morse = ( 
".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
    "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
    "..-","...-",".--","-..-","-.--","--..", " "
)

#making english, into moress code function
def eng_to_morse(text):
    result = ""
    for char in text.lower():
        if char in english:
            result += morse[english.index(char)] + " "
        else:
            print("Error, not english, please type in the alphabet")
    return result.strip()

def morse_to_eng(code):
    result = ""
    letters = code
    for symbol in letters:
        if symbol in morse:
            result += english[morse.index(symbol)]
        else:
            print("Invalid, enter a valid morse code stuff")
    return result

#make the main function
def main():
    print("Welcome to translator for morse code")

    while True:
        print("1. Translate from morse code to english")
        print("2. Translate from English to morse code")
        print("3. Exit")

        choice = input("Coose an option(1-3): ")
        if choice == "1":
            code = input("What is the code you want to ttranslate? ")
            print("Your code says: ")
            print(morse_to_eng(code))
        elif choice == "2":
            text = input("What is the message you need in morse code? ")
            print("Your message says:")
            print(eng_to_morse(text))
        elif choice == "3":
            print("bye")
            break
        else:
            print("Invalid, try again")

main()