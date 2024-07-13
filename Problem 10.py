""" Problem 10: Given a list [4,2,-3,1,6] Write a python program to find if there is a sub-list with sum equal to zero? """

# the given list            
list = [4, 2, -3, 1, 6]

# found_sublist is initialized to False to keep track of until a sublist has been found.
found_sublist = False

# Iterate over each possible starting index of the list
for i in range(len(list)):
    sublist_sum = 0
    # Iterate over possible ending indices of the list starting from i
    for j in range(i, len(list)):
        sublist_sum += list[j]
        
        # Check if the sublist_sum equals zero
        if sublist_sum == 0:
            found_sublist = True
            break                        # Exit inner loop if sublist found
    if found_sublist:
        break                            # Exit outer loop if sublist found

# Check if a sublist with sum equal to zero was found
if found_sublist:
    print("There is a sublist with sum equal to zero.")
else:
    print("No sublist with sum equal to zero found.")
