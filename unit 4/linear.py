#searching
#sorting
#problem1 
user_input = [1,2,3,4,5,6,7,8,9,11]
#check to see if a certain number exist in the user input array
n =14

#linear search 
result = False # vavriable to keep track of the answer 
for e in user_input:
    if e == n:
        result = True
if result == True:
    print('found')

else:
    print('not found')



# if else, for loops, print, calculations(+,-)
    #time: O(n)
input = [1,2,3,4,5]
for i in input:
    print('hi')
    if i == 1:# o(1)
        break


