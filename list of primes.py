def list_of_primes(n):
    lista=[]
    newlist=[]
    for i in range(2, n):
        newlist.append(i)
        for j in range(0, len(newlist)-1-i):
            if newlist[j] > newlist[j+1]:
                newlist[j], newlist[j+1] = newlist[j+1], newlist[j]
    for item in range(len(newlist)):
        for number in range(2, newlist[item]+1):
            if number == newlist[item]:
                lista.append(newlist[item])
            elif newlist[item] % number==0:
                break



    return lista


print(list_of_primes(31))



