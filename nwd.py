def nwd(a,b):
    while a != b:
        if a < b:
            b = b - a
        else:
           a = a - b
    return a

print(nwd(45, 0))



