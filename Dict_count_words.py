def n_letter_dictionary(my_string):
    my_dict = {}                                                        # Init an empty dict
    for word in sorted(my_string.lower().split(),key=str.lower):        # Split the string and iterate over it
        word_length = len(word)                                         # Get the length, also the key
        if word_length in my_dict:                                      # Check if the length is in the dict
            if word not in my_dict[word_length]:                        # If the length exists as a key, but the word doesn't exist in the value list
                my_dict[word_length].append(word)                       # Add the word
        else:
            my_dict[word_length] = [word]
    sort_dict = dict(sorted(my_dict.items()))

    return sort_dict


print(n_letter_dictionary("The way you see people is the way you treat them and the Way you treat them is what they become"))
