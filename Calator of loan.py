# Kalkulator spłaty pozyczki
# Your function for calculating payment goes here
def calloan(principal, annual_interest_rate, duration ):
    p = principal
    r = (annual_interest_rate / 100) / 12
    n = duration * 12
    if r == 0:
        payme = p / n
    else:
        payme = p * (( r * ((1 + r) ** n)) / (((1 + r) ** n) - 1))
    return payme
# Your function for calculating remaining balance goes here
def  calrembal(principal, annual_interest_rate, duration , number_of_payments):
    p = principal
    r = (annual_interest_rate / 100) / 12
    n = duration * 12
    l = number_of_payments
    if r == 0:
        payme =  p * (1 - l / n)
    else:
        payme = p * ((((1 + r) ** n)-((1+r)**l)) / (((1 + r) ** n) - 1))
    return payme
# Your main program goes here
principal=float(input("Enter loan amount: "))
annual_interest_rate=float(input("Enter annual interest rate (percent): "))
duration=int(input("Enter loan duration in years: "))

print("LOAN AMOUNT:",int(principal), "INTEREST RATE (PERCENT):", int(annual_interest_rate))
print("DURATION (YEARS):", int(duration), "MONTHLY PAYMENT:", int(calloan(principal,annual_interest_rate,duration)))

for year in range(1,duration+1):
    print("YEAR:", year, "BALANCE:", int(calrembal(principal,annual_interest_rate,duration,(year*12))) , "TOTAL PAYMENT", int(calloan(principal, annual_interest_rate, duration)*12*year))