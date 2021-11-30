def wielokrot26(n, x):
    while n > x:
        n -= 26
    return n
def cezarIn(klucz, haslo):
    wynik = ""
    for i in range(len(haslo)):
        x = haslo[i]
        y = ord(x) + klucz
        if ord(x) == 32:
            wynik += " "
        elif ord(x) <= 90:
            z = wielokrot26(y, 90)
            wynik += (chr(z))
        else:
            z = wielokrot26(y, 122)
            wynik +=(chr(z))
    return wynik

def cezarOut(klucz, haslo):
    wynik = ""
    for i in range(len(haslo)):
        x = haslo[i]
        y = ord(x) + (26 - klucz)
        if ord(x) == 32:
            wynik += " "
        elif ord(x) <= 90:
            z = wielokrot26(y, 90)
            wynik += (chr(z))
        else:
            z = wielokrot26(y, 122)
            wynik +=(chr(z))
    return wynik

def cezarIn2(tekst, klucz, alfabet):
    wynik = ""
    i = 0
    dIT = len(tekst)
    dIA = len(alfabet)
    while i < dIT:
        j = 0
        while j < dIA:
            if tekst[i] == alfabet[j]:
                wynik += alfabet[(j + klucz)%dIA]
                print(wynik)
            j += 1
        i += 1
        print(i)
    return wynik
