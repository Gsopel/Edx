################### Instructor function ###################
def _create_grades_dict(file_name):
    grade_dict={}
    tests=['Test_1','Test_2','Test_3','Test_4']
    fp=open('student_grades.txt','r')
    lines=fp.readlines()
    fp.close()
    for line in lines:
        elements=line.strip().split(",")
        if elements and elements[0]:
            current_key=elements[0].strip()
            if len(current_key)==10:
                if grade_dict.get(current_key)==None:
                    # Key does not exist. Create it
                    grade_dict[current_key]=[elements[1].strip(),0,0,0,0,0]
                for index in range(2,len(elements),2):
                    current_element=elements[index].strip()
                    if  current_element in tests:
                        grade_dict[current_key][int(current_element[-1])]=int(elements[index+1])
                grade_dict[current_key][5]=sum(grade_dict[current_key][1:5])/4.0
    return grade_dict
def _print_grades(file_name):
    grade_dict=_create_grades_dict(file_name)
    ids=list(grade_dict.keys())
    ids.sort()
    print("{0:^10s} | {1:^16s} | {2:^6s} | {3:^6s} | {4:^6s} | {5:^6s} | {6:^6s} |".format('ID','Name','Test_1','Test_2','Test_3','Test_4','Avg.'))
    for id in ids:
        name=grade_dict[id][0]
        grades=grade_dict[id][1:5]
        average=grade_dict[id][5]
        print("{0:s} | {1:16s}".format(id,name),end="")
        for grade in grades: # Print test scores
            print (" | {0:>6d}".format(grade),end="")
        print(" | {0:>6.2f} |".format(average))

print(_create_grades_dict('file_name'))