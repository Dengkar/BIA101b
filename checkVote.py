#check if user can vote 
# get user age from input
#convert userinput (str)to int() to number
#check if user can vote
#if else statement 
#if above 18, ptint'you can vote'
#get user input
userInput = input('please type ur age')
#convert user input to number
userAge = int(userInput)
#check if user can vote
if userAge >= 18:
    print('you can vote')
else:
    print("you cannot vote")
    