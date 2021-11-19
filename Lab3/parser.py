import csv

from translator import MoviesDB
from unidecode import unidecode
from translator import levenshtein_input_to_MoviesDB_comparison as lev_comapre


def Parse_CSV() -> dict:
    with open('filmy_2.csv', encoding="ISO-8859-2", errors='ignore') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        skipFirst = True
        peopleMovies = {}
        for row in csvReader:
            if skipFirst is True:
                skipFirst = False
                continue
            else:
                movies = {}
                index = 0
                personName = None
                title = None
                points = None

                for column in row:
                    #Title column
                    if index == 0:
                        personName = row[index]
                    #Probably end of the row
                    elif (column == None or column == "") or index > len(row):
                        break
                    #Movie title column
                    elif index % 2 == 1:
                        title = row[index]
                    #If column div is 0 then it's points column
                    elif index % 2 == 0:
                        points = row[index]
                    #When we have both we need to save them
                    if title != None and points != None:
                        movie = lev_comapre(title)[0]
                        movies[movie.lower()] = points
                        title = None
                        points = None
                    index = index + 1
                    personKeyName = personName.lower().replace(' ', '_')
                peopleMovies[personKeyName] = movies

    return peopleMovies


def Parser_neighbours_algorithm_clustering(parsed) -> list:
    data = []
    for person_id, person in enumerate(parsed):
        rated_movies = []
        for movie_id, movie in enumerate(MoviesDB.values()):
            if movie.lower() in parsed[person]:
                rated_movies.append(parsed[person][movie.lower()])
            else:
                rated_movies.append("0")
        data.append(rated_movies)
    return data
