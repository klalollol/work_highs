Dup = set()

def findnumberwithoutpair(arr):
    for i in arr:
        if i in Dup:
            Dup.remove(i)
        else:
            Dup.add(i)
    return Dup.pop()

print(findnumberwithoutpair((input())))