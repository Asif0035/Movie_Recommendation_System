#user_data

users = {
    1 :("young adult", "Sci-Fi"),
    2 :("adult", "Drama"),
    3 :("teen", "Fantasy"),
    4 :("adult", "Action"),
    5 :("young adult", "Comedy")
}

#movie recomendation based on age group, genre, mood

recommendations = {
    ("young adult", "Sci-Fi", "Adventurous") : ["Interstellar" , "Star Wars"],
    ("young adult", "Sci-Fi", "Relaxed") : ["Arrival" , "Contact"],
    ("adult", "Drama", "Thoughtful") : ["The Green Mile" , "The Pursuit of Happiness"],
    ("adult", "Drama", "Melancholy") : ["Beautiful Mind" , "Revolutionary"],
    ("teen", "Fantasy", "Excited") : ["The Hobbit" , "Harry Potter"],
    ("teen", "Fantasy", "Curious") : ["Narnia" , "Lord of the rings"],
    ("adult", "Action", "Energetic") : ["Avengers:Endgame" , "Mission Impossible"],
    ("adult", "Action", "Serious") : ["Inception" , "The Dark Knight"],
    ("young adult", "Comedy", "Funny") : ["Hera Pheri" , "Golmaal"],
    ("young adult", "Comedy", "Relaxed") : ["Dictator" , "Aladin"],
}

user_id = int(input("enter your user id:"))
mood = input("Enter your mood :")
user_profile = users.get(user_id)
recommendation_key = user_profile + (mood,)
recommend_movies = recommendations.get(recommendation_key, ["no recommendation for new users"])
print(f"Recommended movies for user {user_id} in '{mood}' mood: {recommend_movies}")
