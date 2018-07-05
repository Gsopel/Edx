# Type your code here
def construct_list_from_file_sample_(file_name):
    # Make a connection to the file
    file_pointer = open('file_name.csv','r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    out_list = []
    for line in data:
        stripped_line = line.strip('\n')
        out_list.append(stripped_line)
    return out_list


print(construct_list_from_file_sample_('file_name'))