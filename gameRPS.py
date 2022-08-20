import random 
options = [ "rock", "paper", "scissors"]
def is_win(player, opennent):

 if (player=="scisoors" and opennent=='paper') or (player=="paper" and opennent=='rock') or (player=="rock" and opennent=='scissors'):
  return print("you won ")
 elif player == opennent:
    print("tie")
 else:
     print("you lost!!!")
while True:
  user = input ("rock or paper or scissors? or q ro quit  ")
  if user == "q":
    print("ok sorry ")
    quit()
  computer = random.choice(options)
  print(computer)
  is_win(user, computer)
