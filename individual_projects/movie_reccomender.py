#KH 2nd Movie reccomender
import csv

#Function for getting movies
def load_movies():
    #movies list
    movies = []

    try:
        with open("individual_projects/movies.csv", newline = "", encoding = "utf-8") as file:
            reader = csv.DictReader(file)
            #read file and stuff
            for row in reader:
                #try and except so basically convert the csv
                try:
                    movies.append({
                        "title": row["Title"].strip(),
                        "director": row["Director"].strip().lower(),
                        "genres": [g.strip() for g in row["Genre"].lower().split("/")],
                        "actors": [a.strip() for a in row["Notable Actors"].lower().split(",")],
                        "length": int(row["Length (min)"])
                    })
                except:
                    pass
                #if not found, do the keywotd anf say not found
    except FileNotFoundError:
        print("File not found")
    return movies
#function for the filters function
def match_filters(movie, genre, director, actor, min_len, max_len):
    #Check wether the a movie matches all selected files using the and
    if genre and not any(genre in g for g in movie["genres"]):
        return False
    if director and director not in movie["director"]:
        return False
    if actor and not any(actor in a for a in movie["actors"]):
        return False
    if min_len is not None and movie["length"] < min_len:
        return False
    if max_len is not None and movie["length"] > max_len:
        return False

    return True

#Function for printing out all the movies
def print_movie(movie):
    print(
        f'{movie["title"]} - '
        f'Director: {movie["director"].title()} - '
        f'Genres: {"|".join(movie["genres"])} - '
        f'Length: {movie["length"]} min'
    )

#Function for searching movies
def search_movies(movies):
    #get input for the filters
    print("Leave the section of field blank if you want to skip it")
    genre = input("Genre: ").strip().lower()
    director = input("Director: ").strip().lower()
    actor = input("Actor: ").strip().lower()
    
    min_len = input("Min Length, jus blank for none: ").strip()
    max_len = input("Max Length, jus blank for none: ").strip()
    #convert the max and minimum to an integer
    min_len = int(min_len) if min_len else None
    max_len = int(max_len) if max_len else None
    
    print("results:")
    #Basically looks at matching movies and says if no movies match the thing
    found = False
    for movie in movies:
        if match_filters(movie, genre, director, actor, min_len, max_len):
            print_movie(movie)
            found = True

    if not found:
        print("Nothing Matches")

#Function for main menu and call the functions for the chosen actio s
def main():
    print("Movie Reccomender")
    #make a variable for the movies
    movies = load_movies()
    if not movies:#For when the file is invalid or just missing
        print("No movies loadedd")
        return
    #while true loop so it won't end after one action
    while True:
        #print out the choices
        print("Type the number for the action you would like to perform")
        print("1. Search / Get Recommendations")
        print("2. Print Full Movie List")
        print("3. Exit")
        #choice equals the input of the user
        choice = input("choice: ").strip()
        #if the user chooses to search movies, let them choose movies
        if choice == "1":
           search_movies(movies)
        #If they choose to view the list, call the function to view list
        elif choice == "2":
            print("Movie list")
            for movie in movies:
                print_movie(movie)
        #If they want to exit, break the code
        elif choice == "3":
            print("BYe")
            break
        #if the user chooses anything else, just stupid proof it and tell thiem its invalid
        else:
            print("Invalid")
#Call the main function to start the program
main()