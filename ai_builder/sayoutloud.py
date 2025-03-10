def SayOutLoud(num):
  x = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
  text = ""
  dup = dup = [int(digit) for digit in str(num)]
  i = 0
  while i < len(dup):
    c = 1
    while i + 1 < len(dup) and dup[i] == dup[i +1]:
      i+= 1
      c+= 1
    if c > 1:
      text += x[c]
    text +=x[dup[i]]
    i+=1
  return text

print(SayOutLoud(input()))