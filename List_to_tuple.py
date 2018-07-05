def list_to_tuples(MY_LIST):
    rev_list = []
    my_tuple = ()
    for list in my_list:
        list.reverse()
        rev_list.append(tuple(list))
        my_tuple = tuple(rev_list)
    return my_tuple







my_list = [['mean', 'really', 'is', 'jean'],
 ['world', 'my', 'rocks', 'python']]
print(list_to_tuples(my_list))