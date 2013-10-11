def human(num, d):
  if type(num) != int:
    print 'sorry, enter number'
  elif type(d) != dict:
    print 'sorry, enter dictionary'
  else:
    if num % 100 >= 11 and num % 100 <= 15:
      print `num` + " " + d['many']
    elif num % 10 > 1 and num % 10 < 5:
      print `num` + " " + d['two']
    elif num % 10 == 1:
      print `num` + " " + d['one']
    else:
      print `num` + " " + d['many']