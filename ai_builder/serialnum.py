def SerialNumber(strParam):
  sep = strParam.split(".")
  e = list(map(int,(sep[0])))
  o = list(map(int,(sep[1])))
  l = list(map(int,(sep[2])))
  digit = [e,o,l]
  if sum(e) % 2 == 1:
    return "false"
  if sum(o) % 2 == 0:
    return "false"
  for i in  digit:
    if len(i) != 3:
      return "false"
  else:
    if i[-1] > i[-2]  and i[-1] > i[-3]:
      return "true"

# keep this function call here 
print(SerialNumber(input()))