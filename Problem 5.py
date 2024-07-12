""" Problem 5: you have been given a list of N integers which represents the number of mangoes in a bag.
               Each has variable number of mangoes. There are M students in a guvi class, your task is to 
               distribute the mangoes in such a way that each students gets one bag. The difference between
               the number of mangoes in a bag with maximum mangoes and a bag with minimum mangoes given to student is minimum?"""



# List of number of mangoes (N) in the number of bags
N = [5,3,2,4,7]
N.sort()                        # sort the list
min_mango = min(N)              # Variable  to store the bag with minimum mangoes

# Number of bags
no_of_bags = len(N)

# Number of Students(M)
M = int(input("Enter the number of students:"))

# an empty list to store the distributed bags to the students
given_bags = []

if M>no_of_bags:
    print("Students in the class are more than the no. of bags")
else:
    for i in N:                             # iterates through the list of mangoes
        if len(given_bags)<M:               # checks the number of students to distribute
            given_bags.append(i)            # append the distributed bags in the given_bags
print(given_bags)

# Variables to store the bags with maximum and minimum mangoes
min = given_bags[0]
max = given_bags[-1]

# Difference of  the bags with maximum and minimum mangoes
diff = max-min
print(diff)

# To find the difference b/w max and min bag distributed is minimum
if diff <= min_mango:
    print("Minimum")
else:
    print("Not minimum")







