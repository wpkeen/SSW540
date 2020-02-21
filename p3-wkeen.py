# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:32:36 2020

@author: keenw
William Patrick Keen
17th of February, 2020
Stevens Institute of Technology
SSW 540 - Python Assignment #3

This script will take three inputs from the user, pass them to a user defined function and return the max of the three inputs.


Parameters:
    inp1,2,3 - User inputs to the console that are passed to the function

"""


def maxOfThree(num1, num2, num3):
    
    if num1 > num2 and num1 > num3:
        maximum = num1
    elif num2 > num1 and num2 >num3:
        maximum = num2
    else:
        maximum = num3
    print("The maximum of %d, %d, %d is %d" % (num1, num2, num3, maximum))

try: 
    inp1 = int(input("Please enter the first number: \n"))
    inp2 = int(input("Please enter the second number: \n"))
    inp3 = int(input("Please enter the third number: \n"))
    maxOfThree(inp1, inp2, inp3)
except:
    print("Please enter a valid number!")



    
    