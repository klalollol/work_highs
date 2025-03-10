def RemoveBrackets(strParam):
  brackets = list(strParam)
  num_l = 0
  num_r = 0
  for i in range (len(brackets)):
    if brackets[i] == "(":
      num_l +=1
    if brackets[i] == ")":
      num_r +=1

  return  abs(num_l - num_r)

# keep this function call here 
print(RemoveBrackets(input()))