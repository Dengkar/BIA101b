#loop over an array 
fruits = ['a','b','c']
#loop through each element
#at each stage, if the element is 'c'
#print true
for e in fruits: #1.e ='a', 2.e = 'b 3.e ='c'
    if e == 'a':
        print("True from c")
    if e == 'b':
        print('True from b')
#interate over a string
greeting = "Hello"
for char in greeting:
    print(char)
    #Exercise: check if the string 
#iterqte over a range 
for i in range (20):
    print(i) #output: 0 1 2 3 4 5 .....19
    val = i + 5 
    print(val)
#while loops
    #basic while loop
count = 0 
while count < 5:
    print(count)
    count = count + 1
#user input string is unknown 
#print every char of the string 
s = "wonwoo"
counter = 0 
lenth_s = len(s)
print('counter:', counter)
print('len s:', lenth_s)
while counter < lenth_s:
    print('counter:',counter)
    char = s[4]
    print(char)
    counter = counter + 1
    print('-----')

