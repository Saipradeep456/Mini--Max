# 4. Leap Year Checker: Determine if a year is a leap year.

leap = int(input("enter a leap year:"))
if leap%4 == 0 and leap%100!=0:
  print("It is a leap year")
else:
  print("It is not leap year")


  #output:

# enter a leap year:2024
# It is a leap year

# enter a leap year:2025
# It is not leap year


# 4. Leap Year Checker: Determine if a year is a leap year.

import calendar
leap = int(input("enter a leap year:"))
if calendar.isleap(leap):
  print("It is a leap year")
else:
  print("It is not leap year")


  #output:
# enter a leap year:2028
# It is a leap year


# enter a leap year:2029
# It is not leap year

  
  
  