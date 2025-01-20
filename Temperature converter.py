# 8. Temperature Converter: Convert between Celsius and Fahrenheit.

print("temperature converter")
print("choose an option")
print("23.convert celsius to fahrenheit")
print("24 . convert fahrenheit and celsius")

choice = input("enter a 23 or 24")
if choice == "23":
  celsius = float(input("enter a celsius"))
  fahrenheit = (celsius * 9/5) + 32
  print(f"{celsius} is equal to {fahrenheit} fahrenheit")
elif choice == "24":
  fahrenheit = float(input("enter a fahrenheit"))
  celsius = (fahrenheit - 32) * 5/9
  print(f"{fahrenheit}°F is equal to {celsius}°C")



else:
  print("invalid temperature pleaase")


# Output:-

# temperature converter

# choose an option

# 23.convert celsius to fahrenheit
# 24 . convert fahrenheit and celsius
# enter a 23 or 24: 23
# enter a celsius25
# 25.0 is equal to 77.0 fahrenheit

# temperature converter
# choose an option
# 23.convert celsius to fahrenheit
# 24 . convert fahrenheit and celsius
# enter a 23 or 24 :24
# enter a fahrenheit257
# 257.0°F is equal to 125.0°C


# 8. Temperature Converter: Convert between Celsius and Fahrenheit.



def celisus_to_fahrenheit(celsius):
  return (celsius * 9/5)+32

def fahrenheit_celsius(fahrenheit):
  return (fahrenheit -32)*5/9
print(fahrenheit_celsius(100))
print(celisus_to_fahrenheit(37))

# Output:-

# 37.77777777777778
# 98.6
