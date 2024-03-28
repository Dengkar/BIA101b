#input array
array =[3,4,5,6,7,8,9]
target = 9
low = 0
high = len(array) -1
#loop
while low < high:
    # divide 
    mid = low + high // 2 # this is the middle index
    #compare the middle with the target 
    if array[mid] == target:
        print("found")
        break
    # compare and discard the half 
    if target > array[mid]:
        low = mid + 1
    else:
        high = mid -1