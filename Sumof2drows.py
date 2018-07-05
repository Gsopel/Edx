# Type your code here
def sum_2drows(some_list):
    result_list = []

    for sub_list in some_list:
        sum = 0
        for item in range(0,len(sub_list)):
            sum = sub_list[item] + sum
        result_list.append(sum)
    return  result_list

l1 = [[1, 3, 3, 5], [5, -9, -9, 9], [3, 3, 3, 3], [1, 1, 1, 0]]
print(sum_2drows(l1))




