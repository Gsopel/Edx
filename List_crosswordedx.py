################### Instructor function ###################
# Type your code here
def _find_word_horizontal(crossword,word):
    if not crossword or not word:
        return None
    for index,row in enumerate(crossword):
        temp_str=''.join(row)
        if temp_str.find(word)>=0:
            return [index,temp_str.find(word)]
    return None
def _find_word_vertical(crossword,word):
    if not crossword or not word:
        return None
    number_of_columns=len(crossword[0])
    for col_index in range (number_of_columns):
        temp_str=''
        for row_index in range(len(crossword)):
            temp_str=temp_str+crossword[row_index][col_index]
        if temp_str.find(word)>=0:
            return [temp_str.find(word),col_index]
    return None
def _capitalize_word_in_crossword(crossword,word):
    if not crossword or not word:
        return None
    found_position= _find_word_horizontal(crossword,word)
    if found_position:
        for k in range(len(word)):
            crossword[found_position[0]][found_position[1]+k]=crossword[found_position[0]][found_position[1]+k].upper()
        return crossword
    found_position= _find_word_vertical(crossword,word)
    if found_position:
        for k in range(len(word)):
            crossword[found_position[0]+k][found_position[1]]=crossword[found_position[0]+k][found_position[1]].upper()
    return crossword



crosswords1 =[['s','d','o','g'],['c','u','c','m'],['a','x','a','t'],['t','e','t','k']]
crosswords =[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word='cat'
print(capitalize_word_in_crossword(crosswords1,word))