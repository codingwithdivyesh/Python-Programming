# concatinas in python 

name = "divyesh"
last_name = "Modhvadiya"

print(name,last_name) #valid 

print(name + last_name ) # also valid but result no having space 
print(name+" "+ last_name ) # valid and haven't space 

# second way to use concatinas 

name = "divyesh"
last_name = " Modhvadiya "

full_name = name + last_name

print(full_name)

#formated string 

full_name = f" this is my name : {name} .\n this is my last name : {last_name}.\n this is my full name: {full_name} "
print(full_name)