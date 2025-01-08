number = 35 
guess = 0
money =  1



print ( " you have 100 coin to complet this . 1 guess = 1 coin ")


while guess != number:
  guess =  int(input(" type a number : "))
  money += 1 

print ( f"you win this game .after lost {money} coin from 100  ")


 