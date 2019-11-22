def connecting_lights(w, e) :
    m = len(w)
    n = len(e)
    myData= [[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j ==0 :
                myData[i][j]= 0
            elif w[i-1] == e[j-1] :
                myData[i][j]= myData[i-1][j-1] + 1
            else:
                myData[i][j]= max(myData[i-1][j], myData[i][j-1])
    # print(myData)
    index = myData[m][n]
    works = [""] * (index + 1)
    works[index] = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if w[i - 1] == e[j - 1]:
            works[index - 1] = w[i - 1]
            i -= 1
            j -= 1
            index = index - 1
        elif myData[i - 1][j] > myData[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return works

west_side = ['white','red','orange','yellow','green','blue','purple']
east_side = ['green','orange','blue','purple','red','yellow','white']
print(connecting_lights(west_side, east_side))
