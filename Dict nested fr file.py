def construct_nested_dictionary_from_file_sample_(filename):
    my_dictionary = {}
    # set the mode to read mode
    mode = "r"
    # Make a connection to the file
    file_pointer = open('file_names.csv', mode)
    data = file_pointer.readlines()
    for line in data:
        if line[0] != "#":
            # Split the line with the delimiter comma (',')
            first_name, last_name, age = line.strip().split(',')
            if last_name not in my_dictionary:
                my_dictionary[last_name] = {first_name: int(age)}
            else:
                if first_name not in my_dictionary[last_name]:
                    my_dictionary[last_name][first_name] = int(age)

    return my_dictionary




print(construct_nested_dictionary_from_file_sample_('file_name'))