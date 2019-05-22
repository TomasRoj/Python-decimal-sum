# Script for counting decimal sum from a number.

# We ask value from user
number = input("Zadej číslo, z kterého chceš udělat ciferný součet: ")
total = 0

# Now we check if number is positive or negative but not decimal or string.
try:
    # Everything is ok. We process and print the value.
    number = int(number)
  
    # If number is positive
    if (number > 0):
        while (number > 0):
            b = number % 10
            total = total + b
            number = number // 10
        print(total)

    # If number is negative, result is the same but with the "-" mark. So we do the same but print the value with this mark.
    elif (number < 0): 
        # Parsing of negative to positive number using built-in python method.       
        number = abs(number)
        
        while (number > 0):
            b = number % 10
            total = total + b
            number = number // 10

        # Addition of the "-" mark.
        print("-", total)

# The except block checks if number is string or anything else. If yes, it will print error message.
except ValueError:
    print("Číslo může být negativní, ale ne desetinné nebo text atd..")
