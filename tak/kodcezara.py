#Problemy:
#1.Przy deszyfrowaniu kodu program pyta więcej niż jeden raz o klucz
#2.Podczas deszyfrowania litery zmieniane są na DUŻE
#3.Podczas deszyfrowania litery kodu są źle zamieniane



def szyfrowanie(tekst):
    klucz = int(input("Podaj klucz:\n"))
    zaszyfrowany = ""
    for i in range(len(tekst)):
        if ord(tekst[i]) > 122 - klucz:
            zaszyfrowany += chr(ord(tekst[i]) + klucz - 32)
        else:
            zaszyfrowany += chr(ord(tekst[i]) + klucz)
    return zaszyfrowany

def deszyfrowanie(tekst):
    klucz = int(input("Podaj klucz:\n"))
    deszyfrowany = ""
    for i in range(len(szyfrowanie(tekst))):
        if ord(tekst[i]) > 97 - klucz:
            deszyfrowany += chr(ord(tekst[i]) - klucz - 32)
        else:
            deszyfrowany += chr(ord(tekst[i]) - klucz)
    return deszyfrowany

def main(args):
    szylubdeszy = int(input("Co chcesz zrobić:\n"
                        "1 = Szyfrowanie\n"
                        "2 = Deszyfrowanie\n"))

    if szylubdeszy == 1 or szylubdeszy == 2:
        if szylubdeszy == 1:
            tekst = input("Podaj ciąg do zaszyfrowania:\n")
            print("Ciąg zaszyfrowany:\n", szyfrowanie(tekst))
            taknie = int(input("Czy chcesz od razu deszyfrować? Podaj 1=TAK, 2=NIE:\n"))
            if taknie == 1 or taknie == 2:
                if taknie == 1:
                    print("Deszyfrowanie:\n", deszyfrowanie(szyfrowanie(tekst)))
                if taknie == 2:
                    return "nie to nie"
            else:
                return "brak wyboru"
        if szylubdeszy == 2:
            tekst = input("Podaj ciąg do deszyfrowania:\n")
            print("Ciąg deszyfrowany:\n", deszyfrowanie(tekst))
    else:
        return "Zła opcja wyboru"

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))