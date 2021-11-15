import csv


def Parse_CSV():
    data = []
    with open('filmy.csv', encoding="ISO-8859-2", errors='ignore') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        skipFirst = True
        peopleMovies = []
        for row in csvReader:
            if skipFirst is True:
                skipFirst = False
                continue
            else:
                movies = []
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
                        data.append({personName: movies})
                        break
                    #Movie title column
                    elif index % 2 == 1:
                        title = row[index]
                    #If column div is 0 then it's points column
                    elif index % 2 == 0:
                        points = row[index]
                    #When we have both we need to save them
                    if title != None and points != None:
                        movies.append({title: points})
                        title = None
                        points = None
                    index = index + 1
                peopleMovies.append({personName: movies})

    print(peopleMovies)
    return peopleMovies
