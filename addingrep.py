def adding_report():
    while True:
        report = ""
        report = input("Enter T or A:")
        if report.isalpha():
            if report.lower() == "t":
                suma = 0
                while True:
                    putt = input('Enter int or "Q" to quit:')
                    if putt.isdigit():
                        suma = suma + int(putt)
                    elif putt.lower() == "q":
                        return print("Total:", suma)
                    else:
                        return print("Wrong input.")
            elif report.lower() == "a":
                suma = 0
                result = ""
                while True:
                    putt = input('Enter int or "Q" to quit:')
                    if putt.isdigit():
                        result = result + str('\n') + str(putt)
                        suma = suma + int(putt)
                    elif putt.lower() == "q":
                        return print("Items:", result + '\n' + '\n',"Total:", '\n' + str(suma))
                    else:
                        return print("Wrong input.")

            else:
                return print("Input is wrong.")


adding_report()
