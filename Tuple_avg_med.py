# Type your code here
import numpy

def mean_median(some_tuple):

    lenght = len(some_tuple)
    sort_tuple = sorted(some_tuple)

    average = sum(some_tuple) / lenght
    mediana = numpy.median(numpy.array(some_tuple))
    return (average, mediana)








my_tuple = (3, 3, 0, 1, 12, 13, 15, 16)
print(mean_median(my_tuple))