# and , or , NOT

std10_MARKS = 90
std12_MARKS = 70

#! and if both the operands are ture 

# college want minimum 55 marks for admisson in  any single one  ( 10th and 12th )

if std10_MARKS >= 55 and std12_MARKS >= 55:
    print ("you are Eligible for admisson ")
else:
    print (" not Eligible for admisson ")

# college want minimum 55 marks for admisson in  both one ( 10th and 12th )

if std10_MARKS >= 55 or std12_MARKS >= 55:
    print("you are Eligible for admisson ")
else:
    print ( " not Eligible for admisson " ) 

# college want no cirminal record for safty in student 


std10_MARKS = 90
std12_MARKS = 70
criminal = False


if not criminal :
    print ("Eligible")
else:
    print ("Not-Eligible")
