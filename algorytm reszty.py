def interface():
    print("Proszę podać kwotę do rozmiany")
    __NOMINALS = [500, 200, 100, 50, 20, 10, 5, 2]
    while (True):
        try:
            money = int(input())
            coins = change(money, __NOMINALS)
            print("Wydano:")
            for x in range(len(__NOMINALS)):
                print(coins[x], " monety o nominale ",__NOMINALS[x])
        except ValueError:
            print("Nie jest możliwym wydanie takiej reszty, proszę podać inną kwotę.")

def change(money, nominals):
    amount = list()
    for x in range(len(nominals)):
        amount.append( money//nominals[x])
        money %= nominals[x]
    if money!=0:
            raise ValueError
    return amount

interface()
