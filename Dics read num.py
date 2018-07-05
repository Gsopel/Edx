def read_numbers(some_number):
    numbers = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
               9: "nine"}
    result = ""
    stri_some_number = str(some_number)
    for num in stri_some_number:
        num1 = int(num)
        res = numbers.get(num1)
        result = result + str(res) + " "
    stripped = result.rstrip(" ")

    return stripped





some_num = 4721
print(read_numbers(some_num))