
def bubbles(myList):
    for i in range(0, len(myList)-1):
        for j in range(0, len(myList)-1-i):
            if myList[j] > myList[j+1]:
                    myList[j], myList[j+1] = myList[j+1], myList[j]
    return myList

list = [54,26,93,17,77,31,44,55,20]
print(bubbles(list))