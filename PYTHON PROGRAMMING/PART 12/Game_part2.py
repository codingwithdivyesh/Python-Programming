print (" if you want to quit the game just type quit")



number = 35 
guess = 0
money =  1




print ( " you have 100 coin to complet this . 1 guess = 1 coin ")
print ( " Type 'back' if you want to go back " )


while True:
   user = input(" type a number : ").strip()
   if user == "back":
        print(" you clicked back oppstion")
        break
   if user :
      guess = int(user)
      if guess == number :
        print(f"you win this game,after {money} coin ")
        break
      else:
         money+=1
   





  








 