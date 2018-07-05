# Kalkulator spłaty pozyczki

def calloan(principal, annual_interest, duration):
    p = principal
    r = (annual_interest / 100) / 12
    n = duration * 12
    print(r)

    if r == 0:
        payme = p / n
    else:
        payme = p * (( r * ((1 + r) ** n)) / (((1 + r) ** n) - 1))

    return payme


print(calloan(1000.0, 4.5, 5))