    # Type your code here

 def _dictionary_of_word_counts_sample_(sample_string):
    lowered_splitted_string = sample_string.lower().split()
    sample_dictionary = {}
    for word in lowered_splitted_string:
        sample_dictionary[word] = lowered_splitted_string.count(word)
    return sample_dictionary


print(dictionary_of_word_counts("I love that fact that  am in love with python"))
