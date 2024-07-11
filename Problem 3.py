""" Problem 3: Given Python list [10, 501, 22, 37, 100, 999, 87, 351]. find out how many
               numbers are there in the given list which are happy numbers."""


# Given list
list = [10, 501, 22, 37, 100, 999, 87, 351]   
happy_no=0                       # initialise a variable to store count of happy numbers

# iterate through the list
for num in list:
    data = str(num)                 # converts digit to string for iteration
    
    while True:                     # loops infinitely
        sum = 0
        for i in data:              # iterates digit by digit
            sum += int(i) ** 2      # calculate the sum of squares of digits
    
        num = sum
        data = str(num)             # Update n to reflect the new value of num
    
# increment the happy_no by 1 if num is 1 or else breaks   
        if num == 1:
            happy_no+=1
            break
        else:
            break
        
print("Number of Happy numbers:",happy_no)








