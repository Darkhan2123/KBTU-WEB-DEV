def sleep_in(weekday, vacation):
  if(weekday == False or vacation == True):
    return True
  elif(weekday == False and vacation == False):
    return True
  else:
    return False