# 15. Simple Quiz: Create a multiple-choice quiz with a score.
score = 0
print("1. what is your name")
print("a) pradeep")
print("b) deep")
print("c) sri")
print("d) sai")
answer = input("enter a (a/b/c/d)").lower()
if answer == "a":
  score+=1


print("n\2. what is 5+3")
print("a) 7")
print("b) 8")
print("c) 5")
print("d) 4")
answer = input("enter a (a/b/c/d)").lower()
if answer == "b":
  score+=1

print("n\3. what is 7+3")
print("a) 10")
print("b) 8")
print("c) 5")
print("d) 4")
answer = input("enter a (a/b/c/d)").lower()
if answer == "a":
  score+=1

print(score) 


#OUTPUT:- 
# 1. what is your name
# a) pradeep
# b) deep
# c) sri
# d) sai
# enter a (a/b/c/d)a
# n. what is 5+3
# a) 7
# b) 8
# c) 5
# d) 4
# enter a (a/b/c/d)b
# n. what is 7+3
# a) 10
# b) 8
# c) 5
# d) 4
# enter a (a/b/c/d)a
3
