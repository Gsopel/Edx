# Type your code here
def my_final_grade_calculation(filename):
    # Make a connection to the file
    file_pointer = open('final grades.txt','r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    my_dict = {}
    quiz = []
    assigment = []

    for line in data:
        name, q1, q2, q3, q4, q5, q6, a1, a2, a3, a4, midterm, final = line.strip().split(',')
        quiz = [int(q1), int(q2), int(q3), int(q4), int(q5), int(q6)]
        quiz.sort()
        quizz = quiz[2:]
        avg_quiz = sum(quizz) / len(quizz)

        assigment = [int(a1), int(a2), int(a3), int(a4)]
        assigment.sort()
        assigmentt = assigment[2:]
        avg_assigment = sum(assigmentt) / len(assigmentt)

        total = [avg_quiz, avg_assigment, int(midterm), int(final)]
        total_avg = sum(total) / len(total)

        if total_avg >= 60:
            my_dict[name] = "pass"
        else:
            my_dict[name] = "fail"
    return my_dict





print(my_final_grade_calculation('file_name'))





