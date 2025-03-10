def FizzBuzz(num):
  list =[]
  for i in range(1,num+1):
    if i%3 == 0:
      list.append("Fizz")
    if i%5 == 0:
      list.append("Buzz")
    if i%3 != 0 and i%5 != 0:
      list.append(str(i))
  return " ".join(list)

# keep this function call here 
print(FizzBuzz(int(input())))