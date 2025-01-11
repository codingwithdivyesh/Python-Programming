import random
item_list = [ "rock", "paper", "scissor "] 


user_choice = input(" entry your choice  from rock , paper , scissor =  ")
computer_choice = random.choice(item_list)

print (f"your choice = {user_choice} vs Computer choice = {computer_choice} ")

if user_choice == computer_choice:
    print(" Match draw !!!! ")

elif user_choice == "rock":
    if computer_choice == "paper":
        print(" sorry buddy but !!! you loos ")
    else:
        print(" Congras buddy !!! you win ")

elif user_choice == "paper":
    if computer_choice == "scissor":
        print(" sorry buddy but  !!! you loss ")
    else:
        print(" Congras buddy !!! you win ")


elif user_choice == "scissor":
    if computer_choice == "rock":
        print(" sorry buddy but  !!! you loss ")
    else:
        print(" Congras buddy !!! you win " )