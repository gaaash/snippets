def create_phone_number(n):
    stred = []
    for i in n:
        if i == str :
            stred.append(i)
        else:
            stred.append(str(i))
    phoneFormat = "(",stred[0],stred[1],stred[2],")"," ",stred[3],stred[4],stred[5],"-",stred[6],stred[7],stred[8],stred[9]
    return("".join(phoneFormat))