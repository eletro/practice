def mon(m):
  d = {'JANUARY': 1, 'FEBRUARY': 2, 'MARCH': 3, 'APRIL': 4, 'MAY': 5, 'JUNE': 6, 'JULY': 7, 'AUGUST': 8, 'SEPTEMBER': 9, 'OCTOBER': 10, 'NOVEMBER': 11, 'DECEMBER': 12}
  if type(m) != str:
    print 'enter string'
  else:
    if d.has_key(m[:].upper()) == True:
      print d[m.upper()]
    else:
      print 'No such month'