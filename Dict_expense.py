# Type your code here
# The first few lines of the code are here to help you!
def calculate_expenses(filename):
    # Make a connection to the file
    file_pointer = open('file_name_shop.txt', 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    # NOW CONTINUE YOUR CODE FROM HERE!!!
    my_dictionary = {}
    for line in data:
        item, price = line.strip().split(',')

        my_dictionary[item.strip()] = my_dictionary.get(item.strip(), 0) + float(price)
        print(my_dictionary)
    dic = {}
    for k, v in my_dictionary.items():
        dic[k] = '${0:.2f}'.format(round(v, 2))

    L = ([(k, v) for k, v in dic.items()])
    L.sort()

    return L




print(calculate_expenses('file_names'))