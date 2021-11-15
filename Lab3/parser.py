import csv


def Parse_CSV():
    data = []
    with open('filmy.csv', encoding="ISO-8859-2", errors='ignore') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        skipFirst = True
        for row in csvReader:
            if skipFirst is True:
                skipFirst = False
                continue
            else:
                movies = []
                index = 0
                person = []
                title = None
                points = None
                while True:
                    if index is 0:
                        person = row[index]
                    elif index > len(row) - 2:
                        data.append({person: movies})
                        index = 0
                        break
                    elif index % 2 is 1:
                        title = row[index]
                    elif index % 2 is 0:
                        points = row[index]
                        movies.append({title: points})
                    index = index + 1
            print(movies)
    return data
