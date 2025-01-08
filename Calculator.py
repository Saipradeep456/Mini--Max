# Python Program to Make a Simple Calculator In this program, we ask the user to choose an operation for Simple calculator such as add, subtract, multiply and divide.

# Then user enters 2 numbers and result will be displayed based on the operation selected.

print("1 - ADD")
print("2 - substract")
print("3 - multiple")
print("4 - divide")
sai = int(input(" choose a operator "))
if(sai in [1,2,3,4]):
  num1 = int(input("enter a first number"))
  num2 = int(input("enter a second number"))
  if(sai == 1):
    print(num1+num2)
  elif(sai == 2):
    print(num1-num2)
  elif(sai == 3):
    print(num1*num2)
  elif(sai == 4):
    print(num1/num2)

else:
  print("invalid")
   

# output

# 1 - ADD
# 2 - substract
# 3 - multiple
# 4 - divide

#  choose a operator 1
# enter a first number1
# enter a second number2
# 3

# choose a operator 2
# enter a first number6
# enter a second number1
# 5


# choose a operator 3
# enter a first number2
# enter a second number4
# 8


#  choose a operator 4
# enter a first number9
# enter a second number3
# 3.0
