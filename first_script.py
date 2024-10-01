def check_movie_release(movie):
    name, year = movie
    if year < 2000:
        print(f"{name} was released before 2000.")
    else:
        print(f"{name} was released after 2000.")
        return name
    
recent_movies = []



favorite_movies = [

    ("The Matrix", 1999),
    ("Inception", 2010),
    ("The Godfather", 1972),
    ("Interstellar", 2014),
    ("Pulp Fiction", 1994)
]

for movie, year in favorite_movies:
    result=check_movie_release(movie, year)
    if result is not None:
        recent_movies.append(result)

print(recent_movies)