# Type your code here
def construct_dict_from_file_sample_(file_name):
    # Make a connection to the file
    file_pointer = open('file_name.csv','r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    my_dictionary={}
    for line in data:
        name, course1, course2, course3, course4 = line.strip().split(',')
        print(course1,name)
        if int(course1) > 70 and int(course3)>70:

            my_dictionary[name] = [float(course1), float(course2), float(course3), float(course4)]

    return my_dictionary





print(construct_dict_from_file_sample_('file_name'))