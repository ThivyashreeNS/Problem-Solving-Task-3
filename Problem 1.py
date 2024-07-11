""" Problem 1: You have been given a Python list [10, 501, 22, 37, 100, 999, 87, 351] and create two lists,
               one which have all the Even numbers and another list which have all the Odd numbers. """



list = [10, 501, 22, 37, 100, 999, 87, 351]      

# create an empty lists for even & odd numbers
even_list = []                                    
odd_list = []                                      

# iterates through the given list
for i in list:                                     
    if i%2==0:                               # checks if it is divisible by two        
        even_list.append(i)                  # if it is True, append the current iterate in the even list
    else:
        odd_list.append(i)                   # if it is False, append the current iterate in the odd list

# Prints the Even and Odd lists
print("Even numbers of the list:", even_list)
print("Odd numbers of the list:", odd_list)