#Q5. Make a two-player Rock-Paper-Scissors geme. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner)

#Remember the rules:

#Rock basta sclesors R(r) beats S(s)

#Scissors beste paper-> S(a) beats P(p)

#Paper beats rock -> P(p) beets R(r)
# 14. Rock, Paper, Scissors Game: A simple game against the computer

series = int(input("enter the number of series:"))
player1_arr = 0
player2_arr = 0

for i in range(series):
  player1 = input("enter your choice(R,S,P):").upper()
  player2 = input("enter your choice(R,S,P):").upper()

  if player1 == player2:
    print("Draw")
  elif(player1 == "R" and player2 == "s" ) or (player1 == "s" and player2 == "p" ) or(player1 == "p" and player2 == "R" ) :
    print("player1 win")
    player1_arr+=1

  else:
    player2_arr+=1
    print("player2 wins")

if player1_arr > player2_arr:
  print("player1 won the series")
elif player1_arr < player2_arr:
  print("player2 won the series")
else:
  print("The series is a tie")



# OUTPU:-

#enter the number of series:1

#enter your choice(R,S,P):r
#player2 wins
