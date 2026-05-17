movies = {
    "Avatar": 4,
    "Inception": 5,
    "Titanic": 3
}

def add_movie():
    name = input("Enter movie name: ")
    rating = int(input("Enter rating (1-5): "))
    if rating >= 1 and rating <= 5:
        movies[name] = rating
        print("Movie added.")
    else:
        print("Invalid rating.")

def update_movie():
    name = input("Movie to update: ")
    if name in movies:
        rating = int(input("Enter new rating (1-5): "))
        if 1 <= rating <= 5:
            movies[name] = rating
            print("Rating updated.")
        else:
            print("Invalid rating.")
    else:
        print("Movie not found.")

def delete_movie():
    name = input("Movie to delete: ")
    if name in movies:
        del movies[name]
        print("Movie deleted.")
    else:
        print("Movie not found.")

def highest_rated():
    highest = max(movies.values())
    print("Highest Rating =", highest)
    print("Movies having highest rating:")
    for name, rating in movies.items():
        if rating == highest:
            print(name)

def average_rating():
    total = 0
    for rating in movies.values():
        total = total + rating
    avg = total / len(movies)
    print("Average rating =", avg)


# Menu
while True:
    print("\n1.Add 2.Update 3.Delete 4.Highest 5.Average 6.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        add_movie()
    elif ch == 2:
        update_movie()
    elif ch == 3:
        delete_movie()
    elif ch == 4:
        highest_rated()
    elif ch == 5:
        average_rating()
    elif ch == 6:
        break
    else:
        print("Invalid choice.")
