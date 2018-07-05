def  calrembal(principal, annual_interest_rate, duration , number_of_payments):
    p = principal
    r = (annual_interest_rate / 100) / 12
    n = duration * 12
    l = number_of_payments
    if r == 0:
        payme1 =  p * (1 - l / n)
    else:
        payme1 = p * ((((1 + r) ** n)-((1+r)**l)) / (((1 + r) ** n) - 1))
    return payme1

print(calrembal(1000, 10 , 5, 1 ))