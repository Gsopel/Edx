# Type your code here
def multi(a,b):
    len_rowb = len(b)
    len_cola = len(a[0])
    if len_cola == len_rowb:
        return True
    else:
        return False








a = [[2, 3, 4],
     [3, 4, 5]]
b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]
print(multi(a,b))