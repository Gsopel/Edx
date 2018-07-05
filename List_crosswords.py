# Type your code here
def find_word_horizontal(crossword,word):
    # insert the code from your function in part 1 here
    l =[]
    for rows in crossword:
        join_list = "".join(rows)
        if join_list.find(word) != -1:
            return [crossword.index(rows), rows.index(word[0])]

# Type your code here
def find_word_vertical(crosswords, word):
    l = []
    for i in range(len(crosswords[0])):
        l.append(''.join([row[i] for row in crosswords]))
        for line in l:
            if word in line:  # finding index
                row_index = i
                column_index = line.index(word[0])
                return [column_index, row_index]
def capitalize_word_in_crossword(crossword,word):
    horizontal = find_word_horizontal(crossword,word)
    vertical = find_word_vertical(crossword,word)
    if horizontal != None:
        row = crossword[horizontal[0]]
        col = horizontal[1]
        for char in range(col,len(row)):
            row[char] = row[char].upper()
        return crossword
    elif vertical != None:
        row = vertical[0]
        col = vertical[1]
        for rows in range(row,len(crossword)):
            crossword[rows][col] = crossword[rows][col].upper()
        return crossword
    else:
        return crossword



crosswords1 =[['s','d','o','g'],['c','u','c','m'],['a','x','a','t'],['t','e','t','k']]
crosswords =[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word='cat'
print(capitalize_word_in_crossword(crosswords1,word))