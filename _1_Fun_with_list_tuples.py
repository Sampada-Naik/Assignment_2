lst1 = [(1,2),(5,6),(3,0)]

lstlength = len(lst1)
for i in range(0,lstlength):
    for j in range(0,lstlength-i-1):
        if(lst1[j][-1] > lst1[j+1][-1]):
            temp = lst1[j]
            lst1[j] = lst1[j+1]
            lst1[j+1] = temp

print(lst1)