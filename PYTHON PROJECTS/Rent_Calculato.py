rent =int(input("Enter the amount of rent = "))
food =int(input("Enter the amount of food/other expense = " ))
electricitybill =int(input("Enter how much current unite used =  "))
chargeperunit =int(input("Enter how much is the cost on a unit in your area = "))
persons =int(input("Entry the number of people living  =  " ))

unit_bill = electricitybill * chargeperunit

total_bill = (food+unit_bill+rent) // persons 

print (f"your finally bill amount of distribution is = {total_bill}")