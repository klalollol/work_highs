def LargestFour(arr):
  sam = []
  total = 0
  for i in range (0,len(arr)):
    for i in range (4):
      large = max(arr)
      arr.pop(arr.index(large))
      sam.append(large)
    for i in range (0,len(sam)):
      total += sam[i]
    return total


# keep this function call here 
print(LargestFour(input()))