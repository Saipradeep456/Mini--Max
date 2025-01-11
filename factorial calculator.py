# 5. Factorial Calculator: Calculate the factorial of a number


factorial = int(input("enter a factorial number:"))
total = 1
for i in range(1,factorial+1):
  total = total*i
  print(total)

#output :

#enter a factorial number:5
# 1
# 2
# 6
# 24
# 120

# 5. Factorial Calculator: Calculate the factorial of a number

n = int(input("enter a factorial number:"))
factorial = 1
while n>0:
  factorial = factorial*n
  n -=1 # n= n-1
  print(factorial)

  #output :

# enter a factorial number:5
# 5
# 20
# 60
# 120


# 5. Factorial Calculator: Calculate the factorial of a number

def factorial(n):
  if n == 0:
    return 1
  else:
    return n*factorial(n-1)
print(factorial(5))

#output :

# 120

# 5. Factorial Calculator: Calculate the factorial of a number

def factorial_iternation(n):
  result = 1
  for i in range(1,n+1):
    result*=i
  return result
print(factorial_iternation(5))

#output :
  
# 120
