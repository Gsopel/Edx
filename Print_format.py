# Type your code here
# The first few lines of the code are here to help you!
def formatted_print(my_dictionary):
    dic_sorted = sorted(my_dictionary.items(), key=lambda t:t[1], reverse =True)
    for item in dic_sorted:
       print("{0:10s}{1: 6.2f}".format(item[0],item[1]))






my_dic = {'john':34.480, 'eva':88.5, 'alex':90.55, 'tim': 65.900}
print(formatted_print(my_dic))