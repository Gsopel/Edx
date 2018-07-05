# Type your code here
def multiplication_table(n):
    tot_len = n*n
    some_list = []

    new_list = []
    for cols in range(1,n+1):
        for rows in range(1,n+1):
            some_list.append(rows*cols)
    for cols in range(0,tot_len, n):
        new_list.append(some_list[cols:cols+n])

    return new_list








print(multiplication_table(3))