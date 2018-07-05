
def countme(lista, a):
    result = 0
    for i in lista:
        if i == a:
            result = result + 1
    return result





list1 = [77,54, 26, 93, 17, 77, 31, 44, 55, 20]
a = 77
print(countme(list1,a))