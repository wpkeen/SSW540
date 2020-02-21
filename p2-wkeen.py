# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:11:16 2019

@author: keenw

This script will convert a users numerical input into a letter grade by reading an input parameter from the user.
If the user enters a number out of range or the input cannot be cast to a float, it will throw an exception.

"""

#Read in the user input as a string using the input function

grade = input("Please enter your quiz grade:\n")


#Cast the string to a float
try:
    numGrade = float(grade)
    
    #Provide the conditionals for the different grades

    if numGrade <= 100 and numGrade >= 93:
        print("You got an A!")
    elif numGrade < 93 and numGrade >= 90:
        print("You got an A-")
    elif numGrade < 90 and numGrade >= 87: 
        print("You got a B+")
    elif numGrade < 87 and numGrade >= 83:
        print("You got an B")
    elif numGrade < 83 and numGrade >= 80: 
        print("You got a B-")
    elif numGrade < 80 and numGrade >= 70: 
        print("You got a C")
    elif numGrade < 70 and numGrade >= 0:
        print("You got an F")
    else:
        print("The grade you entered is out of range!")

#Throw the exception
except:
    print("Please enter a number.")
    


    
