import datetime

# Data structure to store movies and their ratings
movies_description = {"movies": []}

def welcome_heading():
    return """
     Welcome to Semicolon Movie Rating System Application
     ====================================================
    """

def application_menu():
    return """
      1. Add a Movie
      2. Rate a Movie
      3. View Average Ratings
      4. Exit
    """

def add_a_movie():
    movie = input("Movie Title: ").strip()
    dat = datetime.datetime.now()
    movie_input = {"movie": movie, "date": dat, "ratings": []}
    movies_description["movies"].append(movie_input)
    return f"\n <<< The movie {movie_input['movie']} has been Added Successfully >>>"

def rate_a_movie():
    movie_request = input("Enter The movie Name: ").strip()
    rating = float(input("Enter Your Rating (1-5): "))
    
    for movie in movies_description["movies"]:
        if movie["movie"] == movie_request:
            movie["ratings"].append(rating)
            return f"\n <<< Your rating for {movie_request} has been added successfully >>>"
    
    return f"\n <<< Movie {movie_request} not found >>>"

def view_average_ratings():
    if not movies_description["movies"]:
        return "\n <<< No movies available >>>"
    
    for movie in movies_description["movies"]:
        if movie["ratings"]:
            average_rating = sum(movie["ratings"]) / len(movie["ratings"])
        else:
            average_rating = "No ratings yet"
        print(f"Movie: {movie['movie']}, Average Rating: {average_rating}")
    
    return ""

def main():
    print(welcome_heading())
    
    while True:
        print(application_menu())
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            print(add_a_movie())
        elif choice == "2":
            print(rate_a_movie())
        elif choice == "3":
            print(view_average_ratings())
        elif choice == "4":
            print("\n <<< Exiting the application. Goodbye! >>>")
            break
        else:
            print("\n <<< Invalid choice. Please try again. >>>")

if __name__ == "__main__":
    main()