import random
from datetime import date

class movies:
    def __init__(self ,title ,release_date, genres , number_of_plays):
        self.title = title
        self.release_date = release_date
        self.genres = genres
        self.number_of_plays = number_of_plays

    def play(self):
        self.number_of_plays+=1

    def random_play(self):
        self.number_of_plays = random.randint(0, 100)

    def __str__(self):
        return f"title = {self.title}, release date = {self.release_date}, genres = {self.genres}, number of plays = {self.number_of_plays},"

class series(movies):
    def __init__(self ,episode_number , season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number= episode_number
        self.season_number= season_number

    def __str__(self):
        return f"title = {self.title}, release date = {self.release_date}, genres = {self.genres}, number of plays = {self.number_of_plays}, episode number = {self.episode_number}{self.season_number},"

friends = series(title ="friends", release_date=1994, genres="comedy", number_of_plays = 25, episode_number = "E02", season_number = "S14")
the_crown = series(title ="The crown", release_date=2020, genres="historical", number_of_plays = 44, episode_number = "E01", season_number = "S03")
pianist = movies(title ="pianist", release_date=2001, genres="historical, drama", number_of_plays = 55)
matrix = movies(title ="matrix", release_date=1999, genres="action", number_of_plays = 23)


# Punkt 6 z zadania to Przechowuje filmy i seriale w jednej liście.
# Jake je przechowywac w liscie? Jedyny sposob na jaki wpadlem to ten ponizej
# Taki uklad nie dziala :) list_of_movies_and_series = [friends = series(title = ...]

list_of_movies_and_series = [
    friends,
    pianist,
    the_crown,
    matrix,
]



# Ponizej dwie funkcje ktore daja nam serial i film
def get_series(title):
    for i in list_of_movies_and_series:
        if type(i) == series:
            print("To jest serial " , i)

def get_movie(title):
    for i in list_of_movies_and_series:
        if type(i) == movies:
            print("To jest film " , i)

#Otwarzam film i serial za pomoca funkcji play dzieki czemu liczba wyswietlen wzrasta o 1
friends.play()
print("Liczba odtworzen zwiekrzyla sie o jeden " , friends)

pianist.play()
print("Liczba odtworzen zwiekrzyla sie o jeden " , pianist)


# Szukaj filmu lub serialu po tytule
def search(title_of_series_or_movie_u_wanna_find):
    for elements in list_of_movies_and_series:
        if elements == title_of_series_or_movie_u_wanna_find:
            print("Szukany tytul jest w bibliotece " , title_of_series_or_movie_u_wanna_find)

#Napisz funkcję generate_views, która losowo wybiera element z biblioteki, a następnie dodaje mu losową (z zakresu od 1 do 100) ilość odtworzeń.
def generate_views(): 
    x =random.choice(list_of_movies_and_series)
    x.random_play()
    return x
    #print("Randomowy serial lub film z randomowa liczba wyswietlen " , x)

#Napisz funkcję, która uruchomi generate_views 10 razy.
def generate_views_multiplied_10_times():
    i = 1
    while i < 10:
        generate_views()
        i += 1


print("Bilioteka filmow i seriali")



"""
Wygeneruje odtworzenia treści za pomocą funkcji generate_views.
Wyświetli na konsoli komunikat Najpopularniejsze filmy i seriale dnia <data>, gdzie <data> to bieżąca data w formacie DD.MM.RRRR.
Wyświetli listę top 3 najpopularniejszych tytułów.

i = 0
while i < 4:
    generate_views()
    i+=1
"""
# I tutaj nawet jak generuje 4 przypadkowe seriale i filmy nie wiem jak sie odwolac do max of number_of_plays aby robic topke 3 najpopularniejszych
#pokazuje ze klasa nie jest iterowalna (iterable)
#probowalem append do nowej listy tez nic 
#wlasciwie to pod sam koniec zalamka :D reszta jakos poszla
today = date.today()

print("Najpopularniejsze filmy i seriale dnia " , today)

