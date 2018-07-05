# Type your code here

def find_mismatch(s1, s2):
    lower_s1 = s1.lower()
    lower_s2 = s2.lower()
    error = 0
    count = 0
    if len(lower_s2) == len(lower_s1):
        for i in range(0, len(lower_s1)):
            if lower_s1[i] != lower_s2[i]:
                count += 1
        if count == 1 and len(lower_s2) == len(lower_s1):
            error = 1
        elif count > 1 and len(lower_s2) == len(lower_s1):
            error = 2
        else:
            error = 0
    else:
        error = 2

    return error




str1 = "Hello There"
str2 = "helloothere"

print(find_mismatch(str1,str2))