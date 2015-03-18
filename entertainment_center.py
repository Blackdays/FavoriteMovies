import media
import fresh_tomatoes

#List of ron's favorite movies

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://youtu.be/KYz2wyBy3kc")
avatar = media.Movie("Avatar", "A marine on an alien planet", "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://youtu.be/cRdxXPV9GNQ")
school_of_rock = media.Movie("School of Rock", "Using rock music to learn", "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", "https://youtu.be/3PsUJFEBC74")
ratatouille = media.Movie("Ratatouille", "A rat becomes a star chef in Paris","http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg","https://youtu.be/87q0RD5R4Us")
the_grand_budapest_hotel = media.Movie("The Grand Budapest Hotel", "Adventures of a legendary hotel concierge","http://upload.wikimedia.org/wikipedia/en/a/a6/The_Grand_Budapest_Hotel_Poster.jpg","https://youtu.be/1Fg5iWmQjwk")
the_hunger_games = media.Movie("The Hunger Games", "A really real reality show","http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg","https://youtu.be/SMGRhAEn6K0")

#Lists out movies to be deployed

movies = [toy_story, avatar, school_of_rock, ratatouille, the_grand_budapest_hotel, the_hunger_games]

#Calls the function open_movies_page from fresh_tomatoes to generate the website

fresh_tomatoes.open_movies_page(movies)


