# Type your code here
def create_grades_dict(file_name):
    my_dictionary = {}
    # set the mode to read mode
    mode = "r"
    # Make a connection to the file
    file_pointer = open('student_grades.txt', mode)
    data = file_pointer.readlines()
    D={}
    for line in data:
        line = line.rstrip().split(',')  # split string from .readlines() method by comma.
        line = [x.replace(' ', '') for x in line]  # remove extra space from each element from list's items

        D[line[0]] = [line[1]]  # Select student's ID as  the key of dict

        for t in ['Test_1', 'Test_2', 'Test_3', 'Test_4']:  # Check if tests are in file's data
            if t in line:
                D[line[0]] += [int(line[1 + line.index(t)])]  # If it is then select its value
            else:
                D[line[0]] += [0]  # If it is not then select the value of that test is zero
        D[line[0]] += [sum(D[line[0]][1:]) / len(D[line[0]][1:])]  # Calculate average of Total test's value
    return D

# Your main program starts below this line
def print_grades(file_name):
    # Call your create_grades_dict() function to create the dictionary
    grades_dict=create_grades_dict(file_name)
    print("{0:^10s} | {1:^16s} | {2:^6s} | {3:^6s} | {4:^6s} | {5:^6s} | {6:^6s} | ".format("ID", "Name", "Test_1", "Test_2", "Test_3", "Test_4", "Avg."))
    for key in sorted(grades_dict.keys()):
        print("{0:<10} | {1:<16} | {2:>6} | {3:>6} | {4:>6} | {5:>6} | {6:>6.2f} |".format(key, grades_dict[key][0],  grades_dict[key][1],  grades_dict[key][2], grades_dict[key][3], grades_dict[key][4], grades_dict[key][5] ))


print(print_grades('file_name'))