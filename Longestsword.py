# Type your code here
def find_longest_word(some_string):
    res_string = some_string.split()
    low_string = some_string.lower().split()
    count = 0
    miejsce = 0
    len_list=[]
    result = ""
    for item in low_string:
        len_list.append(len(item))

    result = max(len_list)
    miejsce = len_list.index(result)
    return res_string[miejsce]
s1 = "Hercules was a hero"
print(find_longest_word(s1))