# test

name = input("podaj imie: ")
print("czesc " + name)

##########################################################################
# składnia pythona

a = 5
b = 2

if a > b:
    print("a jest większe od b")

##########################################################################
# typy danych

name = "kamil's channel "
name = 'kamil\'s channel'
name = """kamil's
channel"""

print(name)

a = 10
b = 2.5

print(a + b)

is_sky_blue = True
is_sun_blue = False

print(is_sky_blue)
print(is_sun_blue)

print(type(name))
print(type(a))
print(type(is_sky_blue))
print(type(is_sun_blue))

first = 2
second = "3"

print(str(first) + second)
print(first + int(second))

##########################################################################
# operatory matematyczne

a = 4
b = 2
a = 4.0

print(a+b)  # dodawanie
print(a-b)  # odejmowanie
print(a*b)  # mnożenie
print(a/b)  # dzielenie

print(type(a+b))
print(type(a-b))
print(type(a*b))
print(type(a/b))

print(a % b)  # modulo
print(a ** b)  # potęgowanie

a = 5
a = a + 1  #lub a += 1

print(a)

##########################################################################
# operatory porównania

a = 5
b = 5
print(a == b)  # równe sobie
print(a != b)  # nierówne sobie
print(a > b)  # lewa strona większa
print(a < b)  # prawa strona większa
print(a >= b)  # lewa strona większa lub równa
print(a <= b)  # prawa strona większa lub równa

##########################################################################
# operatory logiczne

a = 5

print(a > 2 and a > 10) # sprawdza czy a jest większe od 2 I czy a jest większe od 10
print(a > 2 or a > 10) # sprawdza czy a jest większe od 2 LUB a jest większe od 10

##########################################################################
# string

name = "kamil"
name2 = "MARTYNA"

print(len(name))  # wyświetla ilość znaków
print(name.capitalize())  # zmienia pierwszą literę na dużą
print(name.upper())  # zmienia wszystkie litery na duże
print(name2.lower())  # zmienia wszystkie litery na małe

print(name[0])  # wyświetla pierwszą literę (indeksowanie zaczynamy od 0 tzn: 0, 1, 2, 3, 4, 5...)
print(name[0:3])  # po znaku ":" piszemy liczbę liter ile ma wyświetlić
print(name[3:])  # wyświetla litery od pewnego momentu do końca

channel = "Jak nauczyć się programowania"
print(channel.split(" "))  # split służy do dzielenia stringa do dzielenia na pojedyńcze słowa

join_string = " "
print(join_string.join(['Jak', 'nauczyć', 'się', 'programowania']))  # służy do łączenia słów

print(name.startswith("K"))  # sprawdza czy string zaczyna się jakąś literą
print(name.startswith("k"))

print(name.endswith("L"))  # sprawdza czy string kończy się jakąś literą
print(name.endswith("l"))

print(name.rstrip("l"))  # usuwa literę z prawej strony
print(name.lstrip("k"))  # usuwa literę z lewej strony

name = "akamila"
print(name.strip("a"))  # uwuwa literę z obu stron

first_name = "Kamil"
last_name = "Brzeziński"

print(first_name + " " + last_name)  # łączymy dwa stringi

join_string = " "
print(join_string.join([first_name, last_name]))  # można to zrobić też metodą join

james_bond = 7

print(str(james_bond).zfill(3))  # przy pomocy zfill podajemy informacje z ilu znaków ma składać się nasz nowy string

##########################################################################
# instrukcje warunkowe

light = input("Jakie jest światło? (red, green, yellow)")

if light == "red":
    print("Czekaj!")
elif light == "yellow":
    print("Przygotuj się!")
elif light == "green":
    print("Jedź!")
else:
    print("Niewłaściwa wartość")

##########################################################################
# pętle while for

number = 1

while number < 6:  # pętla while działa do momentu jak nie spełni się podany warunek
    print(number)
    number = number + 1

for number in range(1, 6):  # pętla for będzie sie wykonywać w zakresie cyfr od (1 do 6>
    print(number)

for number in range(0, 20, 2):  # pętla for będzie sie wykonywać w zakresie cyfr od (0 do 20> ale będzie wypisaywać
    print(number)               # cyfry co dwa elementy

for number in range(0, 10):
    if number == 5:
        continue  # continue przerywa aktualne wywołanie pętli i przechodzi do kolejnego wywołania
    print(number)

for number in range(0, 10):
    if number == 5:
        break  # break zakańcza dalsze wywoływanie pętli jeżeli zostanie spęłniony odpowiedzni warunek
    print(number)

##########################################################################
# struktury danych

names_list = []  # tworzymy liste można to zrobić też tak: names_list = ['Kamil', 'Mariusz']
names_list2 = ["Dominik"]  # tworzymy drugą listę drugim spodobem
names_list.append("Kamil")  # dodajemy osoby do listy
names_list.append("Mariusz")  # dodajemy osoby do listy
names_list.append("Adam")  # dodajemy osoby do listy
names_list.append("Kamil")  # dodajemy osoby do listy
names_list3 = names_list + names_list2  # tworzymy trzecią listę która składa się z pierwszej i drugiej

names_list.reverse()  # odwraca listę
names_list.sort()  # sortuje alfabetycznie listę
names_list.sort(reverse=True)  # sortuje alfabetycznie listę od końca

print(names_list[1])  # wypisuje konkretną osobe z listy (indeksowanie zaczynamy od 0 tzn: 0, 1, 2, 3, 4, 5...)

print(names_list)

print(names_list.count("Kamil"))  # liczy ile razy ktoś znalazł się na liście

print(len(names_list))  # sprawdza ilość osób na liście

print(names_list.pop(0))  # wypisuje konkretną osobe z listy i ją z niej usuwa
                          # (indeksowanie zaczynamy od 0 tzn: 0, 1, 2, 3, 4, 5...)
print(names_list)

names_list.remove("Kamil")  # usuwa osobę z listy
names_list.clear()  # czyści listę

##########################################################################
# struktury danych - tuple

person = ("Kamil", "Brzeziński", 32)  # tworzymy liste której później nie można edytować

print(len(person))  # sprawdzamy rozmiar listy

print(person.count("Kamil"))  # sprawdzamy ilość wystąpień danego elementu

print(person)

##########################################################################
# struktury danych - set

names_set = {"Kamil", "Mariusz", "Kamil"}  # tworzymy liste w której nie występują powtórzenia

names_set = set()  # tworzymy pusty set

names_set.add("Kamil")  # dodajemy coś do set
names_set.add("Dominik")  # dodajemy coś do set

names_set2 = {"Mariusz", "Tytus", "Kamil"}

names_set.remove("Kamil")  # usuwa osobe z set ale jeżeli takiej osoby nie ma to wywali błąd ://
names_set.discard("Dominik")  # usuwa osobe z set ale jeżeli takiej osoby nie ma to nic się nie dzieje

names_set.clear()  # metoda czyści set

names_set3 = names_set.union(names_set2)  # dodajemy do siebie sety

names_set3 = names_set.difference(names_set2)  # porównuje sety

names_set3 = names_set.intersection(names_set2)  # szuka części wspólnych dwoch setów

names_set3 = names_set.symmetric_difference(names_set2)  # szuka elementów spoza części wspólnej

for name in names_set: # wyświetlamy listę ale nie wiemy w jakiej kolejności zostaną wyświetone osoby ://
    print(name)

print(names_set)

##########################################################################
# struktury danych - dictionary

countries_and_capitals = {"Poland":"Warsaw", "Germany":"Berlin"}  # tworzymy słownik
countries_and_capitals['Czechia'] = "Prague"  # dodajemy nowe informacje do słownika

countries_and_capitals.clear()  # czyści nasz słownik
for country in countries_and_capitals.keys():  # wyświetlamy wszystkie klucze z naszego słownika
    print(country)

for capital in countries_and_capitals.values():  # wyświetlamy wszystkie wartości z naszego słownika
    print(capital)

for country, capital in countries_and_capitals.items():  # wyświetlamy wszystkie klucze i wartości z naszego słownika
    print(country + "-" + capital)

print(countries_and_capitals["Poland"])  # wyświetlamy wartość pobraną z danego klucza (jeżeli nie ma danego klucza
                                         # w słowniku dostaniemy błąd)

print(countries_and_capitals.get("Poland"))  # wyświetlamy wartość pobraną z danego klucza (jeżeli nie ma danego
                                             # klucza w słowniku dostaniemy wartość typu NONE)

countries_and_capitals.pop("Poland")  # usuwa wartość znajdującą się pod jakimś kluczem

print(countries_and_capitals.pop("Poland"))  # usuwa wartość znajdującą się pod jakimś kluczem + wyświetla ją

print(countries_and_capitals.popitem()) # usuwa ostatnią wartość do słownika

if "Poland" in countries_and_capitals.keys():  # sprawdza czy dany klucz znajduje się w naszym słowniku
    print("Znaleziono!")
else:
    print("Nie znaleziono!")
print(countries_and_capitals)

##########################################################################
# funkcje


countries_information = {}
countries_information["Polska"] = ("Warszawa", 37.97)
countries_information["Niemcy"] = ("Berlin", 83.02)
countries_information["Słowacja"] = ("Bratysława", 5.45)

def show_country_info(country):
    country_information = countries_information.get(country)
    print()
    print(country)
    print("-----------")
    print("Stolica: " + country_information[0])
    print("Liczba mieszkańców w mln: " + str(country_information[1]))

for country in countries_information.keys():
    print(country)

country = input("Informacje o jakim kraju chcesz wyświetlić? ")
show_country_info(country)




def display_sum(a, b):
    print(a+b)

def print_message():
    print("to jest super wiadomosc")

display_sum(2, 3)

print_message()

##########################################################################
# wyjątki

countries_and_capitals = {"Poland": "Warsaw", "Germany": "Berlin", 'Czechia': "Prague"}

try:  # w bloku try umieszczamy kod który może rzucić błąd
    print(2 / 0)
    print(countries_and_capitals['USA'])
except KeyError:  # tutaj podajemy to co ma się wydarzyć jeżeli w bloku try wystąpi wyjątek
    print("klucz nie został znaleziony")
except ZeroDivisionError:
    print("Nie można dzielić przez 0")
finally:  # wszystko co znajduje się w bloku finally wykona się zawsze
    print("To wykona się zawsze")

print()
print("Jestem tutaj")

##########################################################################
# pliki zapis/odczyt

file = open("countries_and_capitals.txt", "w+")  # otwiera plik tekstowy (w+ oznacza ze plik będzie dostępny do
                                                 #  oczytu i zpaisu)

countries_and_capitals = {"Poland": "Warsaw", "Germany": "Berlin", 'Czechia': "Prague"}

for country, capital in countries_and_capitals.items():  # zapisujemy countries_and_capitals w pliku
    file.write(country + "-" + capital + "\n")  # \n powoduje przeniesienie do kolejnej lini
file.close()  # zamyka plik tekstowy


file = open("countries_and_capitals.txt")

for line in file.readlines():  # wyczytuje wszystkie linie z otwartego pliku
    print(line.strip())  # strip usuwa podwojne przeniesienie do kolejnej lini
file.close()  # zamyka plik tekstowy

##########################################################################