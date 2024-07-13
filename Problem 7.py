""" Problem 7: Write a python program to find the first non-repeating elements in a given list of integers."""
            

# Given list of integers
list=[1,2,3,4,2,1,5,3]

unique = []             # List to store non-repeating elements 
duplicate = []          # List to store repeating elements 

# iterate through the given list
for i in list:
    if i not in unique:          # condition to check the current value is present in the list or not
        unique.append(i)         # if True, append in the unique list
    elif i not in duplicate:     # else, check in the duplicate list and append if not
        duplicate.append(i)  

# iterate through the list again to find non-repeating element
for data in list:
    if data in unique and data not in duplicate:
        print("First non-repeating element:",data)
        break
else:
    print("No non-repeating element found")

    
    