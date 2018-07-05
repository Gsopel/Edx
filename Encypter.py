# Type your code here
def my_encryption(some_string):
    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    secret_key = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"
    new_character=[]
    new_secret=[]
    new_string=[]
    result=""
    key=0
    for i in character_set:
        new_character.append(i)
    for i in secret_key:
        new_secret.append(i)
    for i in some_string:
        new_string.append(i)
    for char in new_string:
        if char in new_character:
            key = new_character.index(char)
            result = result + new_secret[key]
    return result




s1 = "Gosia"
print(my_encryption(s1))