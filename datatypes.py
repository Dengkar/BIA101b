#creation of array 
array1= [1,32,4,"thimphu",5,7]
print (array1)
#retrieving
element1 = array1[0]
element2 = array1[4]
last_element = array1[-5]
print(last_element)
#modified elements 
array1[0]=10
print(array1)
# getting number of elements in an array
no_of_elements = len(array1)
print(no_of_elements)
#slicing 
elements = array1[0:2]
print(elements)
#concatenate list - adding of the list 
arr1 = [1,10]
arr2 = ['thimphu','wangdue']
number_to_check = 2
result = number_to_check in arr1
print('result is',result)
arr3 = arr1 + arr2
print(arr3)
arrVariable = [1,2,3]
arrVariable. append(4)
print(arrVariable)
#insert at a specific index 
arrVariable.insert(1,10)
arrVariable.sort()
#adding to stack
stackVar = []
stackVar.append(4)
stackVar.append(2)
stackVar.append(9)
stackVar.append(1) #4,2,9,1
print('After appending', stackVar)
stackVar.pop()
print('After popping', stackVar)
print('removed elemnt:',elements)
