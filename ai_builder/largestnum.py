def Largestpair(num):
    sep = [str(n) for n in str(num)]
    pair = []
    i= 0
    while i < len(sep):
        if i+1 < len(sep):
             pair.append(int("".join([sep[i],sep[i+1]])))
        else:
            pair.append(int(sep[i]))
        i+=1
    return pair,max(pair)
print(Largestpair(input()))