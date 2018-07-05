# Type your code here
def diction(some_string):
    dictionary = {}
    some_string1 = some_string.replace(" ", "")
    some_string2 = some_string1.lower()
    vowels = 'aeiou'
    for char in vowels:
        if char in some_string2:
            dictionary[char] = some_string2.count(char)
    return dictionary





strin1 = "The cosmos is infinite"
print(diction(strin1))