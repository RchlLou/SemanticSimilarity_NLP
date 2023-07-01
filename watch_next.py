import spacy
nlp = spacy.load('en_core_web_md')

# Current film variable.
planet_hulk = 'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.'


# Declares variables
movie_list = []
sim_movies = []
high_score = 0

# Opens movies.txt file and create list of lines in file. (Strips out '\n' at ends of lines.)  Don't need to close() file, implicit with with open.
with open("movies.txt") as file:
    movie_list = [line.rstrip() for line in file]

# Tokenise planet_hulk synopsis.
current_movie = nlp(planet_hulk)

# Iterates through movie_list
for movie in movie_list:
    # Tokenises each movie in movie list.
    similarity = nlp(movie).similarity(current_movie)

    # If similarity_score > than saved highest sim score, saves new highest similarity score and inserts that movie to the beginning of high scoring movie list.
    if similarity > high_score:
        high_score = similarity
        sim_movies.insert(0, movie)

# Prints recommended watch title.
print(f'\nWe recommend you watch:\n\n{sim_movies[0]}\n')
