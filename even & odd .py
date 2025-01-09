# 3. Even or Odd Checker: Check if a number is even or odd.

num = int(input("enter a number:"))
if num%2 == 0:
  print("It is even number")
else:
  print("It is odd number")


#output 

# enter a number:2
# It is even number

# enter a number:5
# It is odd number




# 3. Even or Odd Checker: Check if a number is even or odd. without using % symbol.

num = int(input("enter a number:"))
if (num//2)*2 == num :
  print(f"the number {num} is even")
else:
  print(f"the number {num} is odd")


#output 
# enter a number:2
# the number 2 is even

# enter a number:5
# the number 5 is odd





#   Example 1: num = 8

# 8 // 2 = 4
# 4 * 2 = 8
# 8 == 8 is True, so the number is even.
# Example 2: num = 9

# 9 // 2 = 4 (the decimal part .5 is discarded)
# 4 * 2 = 8
# 8 == 9 is False, so the number is odd.