def string_splosion(str):
  res = ''
  for i in range(len(str)):
    for j in range(i):
      res += str[j]
  res += str
  return res
