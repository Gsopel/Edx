# Type your code here
# The first few lines of the code are here to help you!
def calculate_grades(file_name):
    # Make a connection to the file
    file_pointer = open('file_names.txt', 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    # NOW CONTINUE YOUR CODE FROM HERE!!!
    my_tuple = ()
    my_list = []
    for line in data:
        # Split the line with the delimiter comma (',')
        name, quiz1_score, quiz2_score, quiz3_score, quiz4_score = line.strip().split(',')
        avr = (int(quiz1_score) + int(quiz2_score) + int(quiz3_score) + int(quiz4_score)) / 4
        temp_list = [name, avr]
        my_list.append(temp_list)
        my_list.sort()

    for list in my_list:
        rev_list = tuple(list)
        my_tuple = my_tuple + (rev_list,)

    return my_tuple




print(calculate_grades('file_names'))