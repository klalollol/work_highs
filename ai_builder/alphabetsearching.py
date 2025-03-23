import string
def AlphabetSearching(strParam):
  count = 0
  alphabet = "abcdefghijklmnopqrstuvwsyz"
  alp_list = list(alphabet)
  t = set(list(strParam))
  text = list(t)
  for i in range (0,len(text)):
    if text[i].isalpha() == False:
      pass
    for y in range (0,26):
      if alp_list[y] == text[i]:
        count +=1
      else:
        pass
  if count == 26:
    return "true"
  else:
    return "false"
  return text

# keep this function call here 
print(AlphabetSearching(input()))