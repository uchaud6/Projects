# Description of project @ https://www.dumas.io/teaching/2021/fall/mcs260/nbview/projects/project1.html

# MCS 260 Fall 2021 Project 1
# Umar Chaudhry
# This is my individual work, and I followed the rules of the project description.

# Declare n variable that will be incremented and run in the whole loop AND gather starting value
n = 0
value = int(input("Starting value: "))

# gather list of values to check for prior membership
list_of_values = []
list_of_values.append(value)

while n < 100:
    #convert value variable to a string to measure the length
    length = len(str(value))
    
    # use if/elif statements to gather the largest digit in the number
    if "9" in str(value):
        largest_digit = 9
    elif "8" in str(value):
        largest_digit = 8
    elif "7" in str(value):
        largest_digit = 7
    elif "6" in str(value):
        largest_digit = 6    
    elif "5" in str(value):
        largest_digit = 5
    elif "4" in str(value):
        largest_digit = 4
    elif "3" in str(value):
        largest_digit = 3
    elif "2" in str(value):
        largest_digit = 2
    elif "1" in str(value):
        largest_digit = 1
    else:
        largest_digit = 0

    # gather new value for MWDPS
    print(value)
    value = (value + largest_digit**length) // 2
    

    #check to see if a value has been repeated and if so, end the loop. Otherwise, add the value to the list of values and increment n
    if value in list_of_values:
        n = 101
        print(value)
        print("looped")
    else:
        list_of_values.append(value)
        n = n + 1

if n == 100:
    print("maxiter") 
    