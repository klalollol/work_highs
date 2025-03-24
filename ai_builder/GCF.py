def GCF(arr):
  x,y = arr[0],arr[1]
  while y !=0:
    x,y = y,x%y
  return x
#nigger


print(GCF(input()))
