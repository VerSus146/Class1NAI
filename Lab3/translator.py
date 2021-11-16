import Levenshtein as lev

# Database of movies based on the excel, but with proper names, just like it would be on a real server
MoviesDB = {
    "Polowanie na Czerwony Październik": "The Hunt for Red October",
    "Rick & Morty": "Rick & Morty",
    "Teoria wielkiego podrywu": "The Big Bang Theory",
    "Waleczne serce": "Braveheart",
    "The Expanse": "The Expanse",
    "Miasteczko South Park": "South Park",
    "Kraina Lodu": "Frozen",
    "Dziennik Bridget Jones": "Bridget Jones's Diary",
    "Kapitan Ameryka: Wojna bohaterów": "Captain America: Civil War",
    "Avengers: Czas Ultrona": "Avengers: Age of Ultron",
    "Terminator 2": "Terminator 2: Judgment Day",
    "Planeta Singli": "Planet Single",
    "List do M.": "Letters to Santa",
    "List do M. 2": "Letters to Santa 2",
    "Forrest Gump": "Forrest Gump",
    "Ex Machina": "Ex Machina",
    "Gran Torino": "Gran Torino",
    "Cicha Noc": "Silent Night",
    "Battleship: Bitwa o Ziemię": "Battleship",
    "Narodziny Gwiazdy": "A Star Is Born",
    "Kapitan Phillips": "Captain Phillips",
    "Grand Budapest Hotel": "Grand Budapest Hotel",
    "Wyjazd integracyjny": "Integration Trip",
    "John Wick": "John Wick",
    "John Wick 2": "John Wick: Chapter 2",
    "John Wick 3": "John Wick: Chapter 3 - Parabellum",
    "Narcos": "Narcos",
    "Terminal": "The Terminal",
    "Ona": "Her",
    "Whiplash": "Whiplash",
    "Diabeł ubiera się u Prady": "The Devil Wears Prada",
    "Dom z papieru": "La Casa De Papel",
    "Snowpiercer": "Snowpiercer",
    "Szpital New Amsterdam": "New Amsterdam",
    "Diuna": "Dune",
    "Jak poznałem waszą matkę": "How I met your mother",
    "Chłopaki z baraków": "Trailer Park Boys",
    "Sherlock": "Sherlock",
    "Ty": "You",
    "Gotham": "Gotham",
    "One Direction: All For One": "One Direction: All For One",
    "Love Death + Robots": "Love, Death & Robots",
    "Wiedźmin": "The Witcher",
    "Babydriver": "Baby driver",
    "Siedem": "Seven",
    "Jak zostalem gangsterem. Historia prawdziwa": "How I became a gangster - true story",
    "The Office": "The Office",
    "Dark": "Dark",
    "Stranger Things": "Stranger Things",
    "The Umbrella Academy": "The Umbrella Academy",
    "House of Cards": "House of Cards",
    "Wiedźmin: Zmora Wilka": "The Witcher: Nightmare of the Wolf",
    "Kod wart miliardy dolarów": "The Billion Dollar Code",
    "Nie czas umierać": "No Time To Die",
    "Lupin": "Lupin",
    "Incepcja": "Inception",
    "W garniturach": "The Suits",
    "Sex education": "Sex education",
    "Doktor House": "House",
    "DOTA: Dragon's Blood": "DOTA: Dragon's Blood",
    "Lucyfer": "Lucifer",
    "Venom: Let There Be Carnage": "Venom 2: Carnage",
    "Gladiator": "Gladiator",
    "Obecność 3: Na rozkaz diabła": "The Conjuring: The Devil Made Me Do It",
    "Czarna Wdowa": "Black Widow",
    "Norbit": "Norbit",
    "The Walking Dead": "The Walking Dead",
    "Veer-Zaara": "Veer-Zaara",
    "Hardcore Henry": "Hardcore Henry",
    "Nawiedzony dwór w Bly": "The Haunting of Bly Manor",
    "Chris Chan: A Comprehensive History": "Chris Chan: A Comprehensive History",
    "This Is Monsters": "This Is Monsters",
    "Kung Fury": "Kung Fury",
    "Planeta skarbów": "Treasure Planet",
    "Squid Game": "Squid Game",
    "Atypowy": "Atypical",
    "Saga 'Zmierzch'": "The Twilight Saga",
    "Joker": "Joker",
    "Mroczny Rycerz powstaje": "The Dark Knight Rises",
    "Kevin sam w domu": "Home Alone",
    "Harry Potter i więzień Azkabanu": "Harry Potter and the Prisoner of Azkaban",
    "Split": "Split",
    "Super zioło": "How high",
    "Różowe lata 70.": "That '70s Show",
    "Zombiebobry": "Zombeavers",
    "Supersamiec": "Superbad",
    "Jestem Bogiem": "Limitless",
    "Rozczarowani": "Disenchantment",
    "Przyjaciele": "Friends",
    "Igrzyska śmierci": "The Hunger Games",
    "Constantine": "Constantine",
    "Daredevil": "Marvel: Daredevil",
    "Czarne lustro": "Black Mirror",
    "Dystrykt 9": "District 9",
    "Matrix": "Matrix",
    "Mr. Robot": "Mr. Robot",
    "Avatar": "Avatar",
    "The 100": "The 100",
    "Trzynaście powodów": "13 Reasons Why",
    "Under The Dome": "Pod kopułą",
    "Modyfikowany węgiel": "Altred Carbon",
    "Podróżnicy": "Travelers",
    "Powrót do przyszłości": "Back to the Future",
    "3%": "3%",
    "Jessica Jones": "Jessica Jones",
    "Spider-Man: Daleko od domu": "Spiderman: Far From Home",
    "Venom": "Venom",
    "Laleczka": "Child's Play",
    "Deadpool": "Deadpool",
    "Deadpool 2": "Deadpool 2",
    "Piękny umysł": "A Beautiful Mind",
    "Kac Vegas": "The Hangover",
    "Hobbit": "The Hobbit",
    "Człowiek-scyzoryk": "Swiss Army Man",
    "Tabu": "Taboo series",
    "Legend": "Legend (2015)",
    "Sex/Life": "Sex/Life",
    "Utalentowany pan Ripley": "The Talented Mr. Ripley",
    "Hannibal": "Hannibal",
    "Kac Wawa": "Kac Wawa",
    "Między słowami": "Lost in Translation",
    "Terminator": "Terminator",
    "Locke": "Locke",
    "Locke & Key": "Locke & Key",
    "Dunkierka": "Dunkirk",
    "Wrogowie publiczni": "Public Enemies",
    "Las Vegas Parano": "Fear and Loathing in Las Vegas",
    "Richard mówi do widzenia": "The Professor",
    "Watchmen. Strażnicy": "Watchmen",
    "Wanted: Weapons of Fate": "Wanted: Weapons of Fate",
    "Podziemny krąg": "Fight club",
    "Rocky Horror Picture Show": "The Rocky Horror Picture Show",
    "Droga do El Dorado": "The Road to El Dorado",
    "Monty Python i Święty Graal": "Monty Python and the Holy Grail",
    "Bękarty wojny": "The Inglorious Bastards",
    "Władca Pierścieni: Drużyna Pierścienia": "The Lord of the Rings: The Fellowship of the Ring",
    "Zapach kobiety": "Scent of a Woman",
    "Mechaniczna pomarańcza": "A Clockwork Orange",
    "Mordercza opona": "Rubber",
    "365 dni": "365 Days",
    "Pogromcy duchów II": "GhostBusters II",
    "Pokój": "The Room",
    "Nerd": "Nerd",
    "Amerykańska rutyna": "American Psycho",
    "Niezniszczalny": "Unbreakable",
    "Dziewczyna z sąsiedztwa": "The Girl Next Door",
    "American Beauty": "American Beauty",
    "Malena": "Malèna",
    "Liga Sprawiedliwych: Zaburzone kontinuum": "Justice League The Flashpoint Paradox",
    "Avengers: Koniec gry": "Avengers: Endgame",
    "Noc oczyszczenia": "The Purge",
    "Seksmisja": "Sexmission",
    "Small World": "Small World",
    "Buntownik z wyboru": "Good Will Hunting",
    "Intouchables": "Nietykalni",
    "K-PAX": "K-PAX",
    "Alicja w Krainie Czarów": "Alice in Wonderland",
    "To nie jest kraj dla starych ludzi": "No Country for Old Men",
    "Obcy": "Alien",
    "Transformers: Wiek zagłady": "Transformers: Age of Extinction",
    "Legion samobójców": "The Suicide Squad",
    "Piła III": "Saw III",
    "Kobiety mafii": "Women of Mafia",
    "Szeregowiec Ryan": "Saving Private Ryan",
    "Kompania braci": "Band of Brothers",
    "Pacyfik": "The Pacific",
    "Top gun": "Top gun",
    "Midway": "Midway",
    "Alexander": "Alexander",
    "Patriota": "The Patriot",
    "Bitwa pod Wiedniem": "The Day of the Siege: September Eleven 1683",
    "1920 Bitwa warszawska": "Battle of Warsaw 1920",
    "Tajemnica Westerplatte": "1939 Battle of Westerplatte",
    "Pearl Harbor": "Pearl Harbor",
    "The Office PL": "The office PL",
    "Pewnego razu... w Hollywood": "Once Upon a Time ... in Hollywood",
    "Interstellar": "Interstellar",
    "Wikingowie": "Vikings",
    "Gra o Tron": "Game of thrones",
    "Młody Sheldon": "Young Sheldon",
    "Big Short": "Big Short",
    "Wilk z Wall Street": "The Wolf of Wall Street",
    "Głowa rodziny": "Family Guy",
    "BoJack Horseman": "BoJack Horseman",
    "Peaky Blinders": "Peaky Blinders",
    "Brytania": "Britannia",
    "Westworld": "Westworld",
    "Gambit królowej": "The Queen's Gambit",
    "Avengers: Wojna bez granic": "Avengers: Infinity War",
    "Politics": "Polityka",
    "Breaking Bad": "Breaking Bad",
    "Skazani na Shawshank": "The Shawshank Redemption",
    "Kler": "Clergy",
    "Boże Ciało": "Corpus Christi",
    "Nomadland": "Nomadland",
    "Lot nad kukułczym gniazdem": "One Flew Over the Cuckoo's Nest",
    "Milczenie owiec": "The Silence of the Lambs",
    "Władca Pierścieni": "The Lord of the Rings",
    "Dwóch i pół": "Two and a Half Men",
    "Gra": "The Game",
    "Xtro": "Xtro",
    "Na rauszu": "Another Round",
    "Nagi instynkt": "Basic Instinct",
    "Turbo Kid": "Turbo Kid",
    "Palm Springs": "Palm Springs",
    "Noc przez dwanaście lat": "A Twelve-Year Night",
    "Nowiny ze świata": "News of the World",
    "Kronika świąteczna": "The Christmas Chronicles",
    "Niebo o północy": "The Midnight Sky",
    "Proces Siódemki z Chicago": "The Trial of the Chicago 7",
    "Tenet": "Tenet",
    "Skazany": "Shot Caller",
    "Le Mans '66": "Ford v Ferrari",
    "Na noże": "Knives Out",
    "Donnie Brasco": "Donnie Brasco",
    "Dżentelmeni": "The Gentlemen",
    "Jojo Rabbit": "Jojo Rabbit",
    "Irlandczyk": "The Irishman",
    "Proceder": "Proceder",
    "Latarnia morska": "Lighthouse",
    "Elfy": "Elfs",
    "Cicha noc, śmierci noc II": "Silent Night, Deadly Night Part 2",
    "Bohemian Rhapsody": "Bohemian Rhapsody",
    "Gwiezdne wojny: Skywalker. Odrodzenie": "Star Wars: The Rise of Skywalker",
    "Glass": "Glass",
    "Parasite": "Parasite",
    "Botoks": "Botoxx",
    "Smoleńsk": "Smolensk",
    "Lista Schindlera": "Schindler's List",
    "Pianista": "The Pianist",
    "Full Metal Jacket": "Full Metal Jacket",
    "Wróg u bram": "Enemy at the Gates",
    "Helikopter w ogniu": "Black Hawk Down",
    "Jeniec: Tak daleko jak nogi poniosą": "As Far as My Feet Will Carry Me",
    "Pingwiny z Madagaskaru": "The Penguins of Madagascar",
    "Wall-E": "Wall-E",
    "Shrek 4": "Shrek 4",
    "Kubuś Puchatek": "Winnie-the-Pooh",
    "Epoka lodowcowa 2: Odwilż": "Ice Age: The Meltdown",
    "Tekken": "Tekken",
    "Rocky": "Rocky",
    "Podwodna bestia": "Supershark",
    "Ogniem i mieczem": "With Fire and Sword",
    "Miś": "Teddy Bear",
    "Kill Bill": "Kill Bill",
    "Pięćdziesiąt Twarzy Greya": "Fifty Shades of Grey",
    "Fineasz i Ferb": "Phineas and Ferb",
    "D-Day": "D-Day",
    "Pitbull": "Pitbull",
    "Szybcy i wściekli": "Fast & Furious",
    "Wyspa": "The Island",
    "Wielki Gatsby": "The Great Gatsby",
    "Wyspa tajemnic": "Shutter Island",
    "Prawo zemsty": "Law Abiding Citizen",
    "Shrek": "Shrek",
    "Numer 23": "The Number 23",
    "Ace Ventura: Psi detektyw": "Ace Ventura: Pet Detective",
    "Harry Potter i Zakon Feniksa": "Harry Potter and the Order Of The Phoenix",
    "U nas w Filadelfii": "It's Always Sunny in Philadelphia",
    "Egzorcysta III": "The Exorcist III",
    "Black Dynamite": "Black Dynamite",
    "Na Wspólnej": "Na Wspólnej",
    "Prawo ulicy": "The Wire",
    "Rodzina Soprano": "The Sopranos",
    "Blade Runner": "Blade Runner",
    "Ucieczka z Nowego Jorku": "Escape from New York",
    "Coś": "The Thing",
    "Wielka draka w chińskiej dzielnicy": "Big Trouble in Little China",
    "Oni żyją": "They Live",
    "Kasyno": "Casino",
    "Doktor Strange": "Doctor Strange",
    "Thor: Ragnarok": "Thor: Ragnarok",
    "Dzikie łowy": "Hunt for the Wilderpeople",
    "Oldboy": "Oldboy",
    "W Pogoni": "Chaser",
    "Snajper": "Sniper",
    "Wesele": "The Wedding",
    "Harry Potter": "Harry Potter",
    "Infiltracja": "The Departed",
    "Niezniszczalni": "The Expendables",
    "M jak milość": "M jak milość",
    "Moda na sukces": "The Bold and the Beautiful",
    "Mandalorian": "The Mandalorian",
    "Bad Boys": "Bad Boys",
    "Spider-man": "Spider-man",
    "Transformers": "Transformers",
    "Ocean's Twelve: Dogrywka": "Ocean's Twelve",
    "Django": "Django",
    "Creed Narodziny legendy": "Creed",
    "Brickleberry": "Brickleberry",
    "Dragon Ball Z": "Dragon Ball Z",
    "Kung Fu Panda": "Kung Fu Panda",
    "Pulp Fiction": "Pulp Fiction",
    "Beavis i Butt-Head": "Beavis and Butt-Head",
    "Złotopolscy": "Złotopolscy",
    "Rambo": "Rambo",
    "Plebania": "Plebania",
    "Gomorra": "Gomorrah",
    "Chłopcy z ferajny": "Goodfellas",
    "Człowiek z blizną": "Scarface",
    "300": "300",
    "Tomb Raider": "Tomb Raider",
    "Kiler": "The Hitman",
    "Psy": "Pigs",
    "Psy 2: Ostatnia krew": "Pigs 2: The Last Blood",
    "Toy Story": "Toy Story",
    "Kapitan Jastrząb": "Captain Tsubasa",
    "Sonic. Szybki jak błyskawica": "Sonic the Hedgehog",
    "Egzorcysta": "The Exorcist",
    "Skok przez płot": "Over the Hedge",
    "Zmierzch": "Twilight",
    "Twój Vincent": "Loving Vincent",
    "Chłopaki nie płaczą": "Boys Don't Cry",
    "Ojciec chrzestny": "The Godfather",
    "Spider-Man 2": "Spider-Man 2"
}


# Take user input from CSV ( Excel from our class ) and compare it to MoviesDB created above
def levenshtein_input_to_MoviesDB_comparison(user_input):
    found_movie = (None, 0.0)
    found_translated = False
    for key in MoviesDB:
        movie = levenshtein_ratio(user_input, key)
        if movie is not None:
            # If found movie is ~100% similar ( allowed ~0.09% of difference ) we take it as our correct answer
            if movie[1] > 99.9:
                found_movie = movie
                break
            # Else set the movie we found as currently best and look for better match
            elif movie[1] > found_movie[1]:
                found_movie = movie

    # If previously found best movie is less than 80% match, we look through values of our MoviesDB dictionary
    if found_movie[1] < 80.0:
        for value in MoviesDB.values():
            movie = levenshtein_ratio(user_input, value)
            if movie is not None:
                if movie[1] > 99.9:
                    found_translated = True
                    found_movie = movie
                    break
                elif movie[1] > found_movie[1]:
                    found_translated = True
                    found_movie = movie

    # If the name was found in other language, get it's name in english
    if found_translated is False and found_movie[0] is not None:
        found_movie = MoviesDB[found_movie[0]]
    # Return best found movie ( most close to user_input )
    return found_movie


# This function is checking if the keys and values from MoviesDB are similar to user_input
def levenshtein_ratio(user_input, check):
    # Threshold for Levenshtein comparison. Anything below 75% similarity is going to be counted as not similar.
    lev_threshold = 70.0
    # Ratio is the similarity %, but it's return value is a float in a range of 0 to 1, so we multiply it for easy use
    # It's using InDel distance method to measure similarity
    ratio = lev.ratio(user_input, check) * 100
    # If similarity % is higher than set threshold, return found movie in a tuple
    # (<Movie Name> : string,<Similarity %> : float)
    if ratio > lev_threshold:
        return (check, ratio)

    # Otherwise if not in threshold, return None
    return None
