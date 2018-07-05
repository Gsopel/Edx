def find_integer_with_most_divisors(input_list):
    lista=[]
    for i in range(len(input_list)):
        count = 0
        for j in range(input_list[i]):
            mod = j+1
            if input_list[i] % mod == 0:
                count = count + 1
        lista.append(count)
    res = lista[0]
    for item in lista:
        if item > res:
            res = item
    return input_list[lista.index(res)]



input_list = [8, 44, 12, 200]
print(find_integer_with_most_divisors(input_list))