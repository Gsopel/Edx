
def nww(z,x):
    result = (z*x) / nwd(z, x)
    return int(result)
def nwd(a,b):
    while a != b:
        if a < b:
            b = b - a
        else:
           a = a - b
    return a


print(nww(6,12))
