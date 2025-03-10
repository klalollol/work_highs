def TrappingWater(arr):
  building = []
  max1,max2 = 0,0
  num = 0
  for i in arr:
    if i > max1:
      max2=max1
      max1 = i
    elif i > max2 and i != max1:
      max2 = i
  f = arr.index(max2)
  l = arr.index(max1)      
  for i in range (f-1,l+1):
    building.append(arr[i])
    # print(building)
  for i in  range (0,len(building)):
    if max2 == 1:
        max2 = max1
    if building[i] == max1:
      pass
    if building[i] == max2:
      pass
    else:
      num += max2-building[i]
  return num


# keep this function call here 
print(TrappingWater(input()))