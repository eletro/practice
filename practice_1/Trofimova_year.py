def calend():
  year = input("Enter year: ")
  if type(year) != int:
    print 'please, enter number'
  else:
    if year%400 == 0:
      print 'Leap'
    elif year%100 == 0:
      print 'not leap'
    elif year%4 == 0:
      print 'Leap'
    else:
      print 'not leap'