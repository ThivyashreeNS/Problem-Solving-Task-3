""" Problem 6: You have been given three lists. Your task is to find the duplicates in the 
               list. Write a python program for the same."""
            
# Defining a function
def duplicates(list): 
    # creating empty lists to store the unique and duplicate values
    unique = []
    duplicate = []
    
    for i in list:
        if i not in unique:         # condition to check the current value is present in the list or not
            unique.append(i)        # if True, append in the unique list
        elif i not in duplicate:    # else, check in the duplicate list and append if not
            duplicate.append(i)     
    print("The duplicates in the" ,list, ":",duplicate)
               
list_1=[2,5,3,2,5]
list_2=[6,9,8,6,7]
list_3=[10,12,11,12]

# function calling using parameter
duplicates(list_1)
duplicates(list_2)
duplicates(list_3)

