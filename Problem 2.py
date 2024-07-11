""" Problem 2: You have been given a Python list [10, 501, 22, 37, 100, 999, 87, 351]. Count all the
               Prime numbers and create a new Python list which contains all the Prime numbers in it."""


# Given list
list = [10, 501, 22, 37, 100, 999, 87, 351]    
prime_no = []                                 # empty list to store the prime numbers


#the outer loop iterates through the list
for i in list:
      count=0                                 # temporary variable to store the no. of divisors
      for j in range(1,i+1):                  # inner loop to find the divisors
          if i%j==0:
              count+=1                        # increment the temp variable

      # checks it has only 2 divisors
      if count==2:                           
          prime_no.append(i)                # appends the current iterator to the empty list

no_of_prime = len(prime_no)                 # returns the count of prime numbers

# prints the Prime numbers 
print("No. of Prime Number in the list:", no_of_prime)
print("Prime Number in the given list:",prime_no)





