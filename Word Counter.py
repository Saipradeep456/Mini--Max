# 10. Word Counter: Count the number of words in a string

a = input("enter a string")
print(len(a.split()))

# OUTPUT:-

# enter a stringSAI SAII PRADEEP
# 3


# 10. Word Counter: Count the number of words in a string

def word_counter(input_string):
  words = input_string.split()
  return len(words)

num = input("enter a words :")
print(f"no of words are  {word_counter(num)}")

# OUTPUT:-

# enter a words :bombothula dwaraka sri sai pradeep
# no of words are  5
