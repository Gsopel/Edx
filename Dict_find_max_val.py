# Type your code here
def one_to_2D(some_list, r, c):
    new_list = []
    temp_list = []
    tot_len = r * c
    if tot_len <= len(some_list):
        temp_list = some_list[0: tot_len]
    else:
        none_list = some_list
        for item in range(len(some_list),tot_len):
            none_list.append(None)
    for cols in range(0,tot_len, c):
        temp_list = some_list[cols:cols+c]
        new_list.append(temp_list)
    return new_list







print(one_to_2D([1, 2, 3, 4], 3, 4))