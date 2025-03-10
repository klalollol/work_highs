def DashInsert(strParam):
  result = ""
  sep =[str(num) for num in strParam]
  for i in range (len(sep)):
    result += sep[i]
    if int(sep[i]) % 2 ==1 and int(sep[i+1]) % 2 ==1:
      result +="-"
  return result

print(DashInsert(input()))