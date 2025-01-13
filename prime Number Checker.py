# Prime Number Checker: Check if a number is prime.

def sai_pradeep(n):
  if n <= 1:
    return False
  for i in range(2,n):
    if n%i ==0:
      return False
    return True
print(sai_pradeep(4))

#output:-

# False




# Prime Number Checker: Check if a number is prime.

def sai_pradeep(n):
  if n <= 1:
    return False
  for i in range(2,n):
    if n%i ==0:
      return False
    return True
print(sai_pradeep(5))



#output:-

# True