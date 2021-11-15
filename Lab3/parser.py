import csv
import json


def test():
    with open('filmy.csv', encoding="ISO-8859-2", errors='ignore') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        skipFirst = True
        data = []
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
                    elif index % 2 is 1:
                        title = row[index]
                    elif index % 2 is 0:
                        points = row[index]
                        movies.append({title: points})
                    elif row[index] is None:
                        data.append({person: {json.dumps(movies)}})
                        index = 0
                        break
                    index = index + 1
            print(movies)