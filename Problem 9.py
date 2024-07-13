""" Problem 9: A given Python list[10,20,30,9] and a value 59. Write a Python program to 
               find the triplet in the whose sum is equal to the given value."""
            
# Given list and value
list = [10, 20, 30, 9]
value = 59

print("The given list:",list)
print("The given value:",value)

# Using sum() to get the value of sum of given list
sum = sum(list)

# iterate through the list to find the triplet
for i in list:
    if sum-i == value:      # checks if 'i' is subtracted from the sum of the list is equal to the given value
        list.remove(i)      # if condition is true, remove the current data from the list
        break               # break statement to stop the iteration, if the triplet is found.
    else:
        print("No triplet found in the list.")

print("The Triplet in the list:",list)


