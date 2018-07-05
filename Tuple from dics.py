# Type your code here
def nested_tuple(sample_dict):
    numbers = sample_dict.keys()
    letters = sample_dict.values()
    my_num,my_let = tuple(numbers), tuple(letters)
    return (my_num, my_let)








input_dictionary = {1:"a", 2:"b", 3:"c", 4:"d"}
print(nested_tuple(input_dictionary))