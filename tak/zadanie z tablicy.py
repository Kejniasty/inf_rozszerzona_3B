"zadanie 1"

liczba = int(input("Podaj liczbę: "))
potęga = int(input("Podaj potęgę: "))

if potęga == 0:
    wynik = 1
else:
    wynik = liczba ** (potęga - 1) * liczba

print(wynik)

"zadanie 2"

def seq(n):
    if n == 1:
        return 1
    else:
        return ((-n) * seq(n - 1) + 4)

print(seq(5))

