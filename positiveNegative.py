#objectives
# create a program tha takes in user input 
#and determines if the number is positive or negative 
#input:"your number is positive "or " your number is negative"
#if else
#*print()
#*input()
#!3 mis
#breka down the problem 
#1 take in user input 
#check the TYPE of the input 
#if the type is string, how do you convert it to an int
#2 check if the number is positive or neagtive or zero
# need to use if else statement 
#! a == b (is it equal to)
#! a! = b ( not equal to )
#! a > b ( is a grester than b)
#! a < b (is a less than b)
#! a>= b(is a greater than or equal to b)
#! a <= b (is a less than or equal to b)
# you will be comapring numbers and not string
#3 print thr result 
userInput = input()
userInputType = type(userInput)
print("the type of user input is:', userInputType")
userInputNumber = float(userInput)
print("the type of userInput is :', type(userInputNumber)")
if userInputNumber > 0:
    print('the number is positive')
elif userInputNumber < 0 :
    print('the number is negative')
elif userInputNumber == 0:
    print('the number is Zero')