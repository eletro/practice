def mon(m):
  d = {'january' : 1,'february' : 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}
  if type(m) != str:
    print 'enter string'
  else:
    if d.has_key(m):
      print d[m]
    else:
      print 'wrong month'