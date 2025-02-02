#Armstrong Number in Python
#Check Whether a Given Number is an Armstrong Number or Not
#Given an integer input, the objective is to check whether or not the given input variable is an Armstrong number. In order to do so, we check whether the sum of the digits of each number to the power the length of the number is equal to the number itself or not. If the number is the same as the original, it’s an Armstrong number. Mentioned below are a few of the Methods used to solve this problem

def is_armstrong(number):
  num_str =str(number) 
  num_digits = len(num_str)

  Armstrong_sum = sum(int(digit)**num_digits  for digit in num_str)
  return Armstrong_sum == number

sai = int(input("enter a number:"))
if is_armstrong(sai):
  print("it is amstrong number")
else:
  print("it is not amstrong numer")

  #OUTPUT:-
#   enter a number:153
# it is amstrong number

# enter a number:96
# it is not amstrong numer


