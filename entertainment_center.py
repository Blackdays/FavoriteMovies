import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://youtu.be/KYz2wyBy3kc")
#print(toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on an alien planet", "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://youtu.be/cRdxXPV9GNQ")
#print(avatar.storyline)
#avatar.show_trailer()

school_of_rock = media.Movie("School of Rock", "Using rock music to learn", "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", "https://youtu.be/3PsUJFEBC74")
ratatouille = media.Movie("Ratatouille", "A rat becomes a star chef in Paris","http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg","https://youtu.be/87q0RD5R4Us")
midnight_in_paris = media.Movie("Midnight in Paris", "Going back in time to meet authors","http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg","https://youtu.be/BYRWfS2s2v4")
the_hunger_games = media.Movie("The Hunger Games", "A really real reality show","http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg","https://youtu.be/SMGRhAEn6K0")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, the_hunger_games]
fresh_tomatoes.open_movies_page(movies)
