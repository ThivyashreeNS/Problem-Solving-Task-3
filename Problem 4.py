""" Problem 4: Write a Python program to find the sum of the first and last digit of an integer"""

num = 1234

# converting int to string
num = str(num)

# converting string to int and stores in the variables
first_digit = int(num[0])
last_digit = int(num[-1])

# Adding the first and last digit
sum = first_digit + last_digit

print("Sum of first and last digit of the integer:",sum)
