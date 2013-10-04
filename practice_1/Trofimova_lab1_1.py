def humanizer(num, d):
  if type(num) != int:
    print 'enter the number'
  elif type(d) != dict:
    print 'secord parameter should be dictionary'
  else:
    i = 0:
    while i < 16:
      if i == 1:
        d[i] = 'chas'
      elif i > 1 and i < 5:
        d[i] = 'chasa'
      else:
        d[i] = 'chasov'
      i += 1
    if d.has_key(num%100):
      print `num` + " " + d[num%100]
    else:
      print `num` + " " + d[num%10]