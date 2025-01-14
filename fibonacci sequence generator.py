# 6. Fibonacci Sequence Generator: Generate Fibonacci numbers up to a given limit. 
def fibnonacci_sai(limit):
  fibon_series =[]
  a,b = 0,1
  while a <= limit:
    fibon_series.append(a)
    a,b = b , a+b
  return fibon_series

print(fibnonacci_sai(100))


#OUTPUT:-

# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]