def first_half(str):
  res = ''
  length = len(str)
  for i in range(length / 2):
    res += str[i]
  return res