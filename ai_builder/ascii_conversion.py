def ASCIIConversion(strParam):
  asc = [str(ord(c)) for c in strParam]
  for i in asc:
    if i == "32":
      asc[asc.index(i)] = " "
  return "".join(asc)

# keep this function call here 
print(ASCIIConversion(input()))