import csv
from unidecode import unidecode
from translator import levenshtein_input_to_MoviesDB_comparison as lev_comapre

def Parse_CSV():
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
                        print('original: ',title)
                        movie = lev_comapre(title)[0]
                        print('search: ',movie)
                        #Lower case and unidecode special letters ( śćż )  to normal letters
                        movies[movie.lower()] = points
                        title = None
                        points = None
                    index = index + 1
                    personKeyName = unidecode(personName.lower()).replace(' ', '_')
                peopleMovies[personKeyName] = movies

    print(peopleMovies)
    return peopleMovies
