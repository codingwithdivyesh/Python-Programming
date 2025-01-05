
roll_number = input("entry your roll number : ")

marks_math = int(input("entry your maths number here :"))

if marks_math >= 90:
    print ( " you are : pass with A grade ")
elif marks_math >= 70:
    print ( " you are : pass with B gread ")
elif marks_math >= 50:
    print ( " you are : pass with c gread ")
elif marks_math >= 40:
    print ( " you are : pass with d gread ")
   

    print ( f"Conditionals, rollnumber \"{roll_number}\" you are passed with {marks_math} number in maths ")
else:
    print ( f" sorry , \"{roll_number}\" but your are not qualified for next class ")
  
