s = 'azcbobobegghakl'
word = 'bob'
count = 0

if word[0] in s:
    check = 0
    tempcount = 1
    for item in s:
        if item == word[tempcount-1]:
            tempcount +=1
            if tempcount == len(word):
                count += 1
                tempcount = 1
        else:
            tempcount = 1



print("Number of times bob occurs is: ", count)