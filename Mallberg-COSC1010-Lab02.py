# Marit Mallberg
# UWYO COSC 1010
# Submission Date: 9/17/2024
# Lab 02 
# Lab Section: 10
# Sources, people worked with, help given to: Grady, and there were two girls sitting next to me and we helped each other.

your_variable_here = "when you see this, replace it with your code"

## Section ONE

# Complete the following print statement to print out "Hello, COSC1010"
print("Hello, COSC1010")

# Assign the string above to a variable named hello_message and print that variable
hello_message = "hello, COSC1010"
print(hello_message)

# Assign the string "cowboy joe" to a variable, and print that variable with title casing
name="cowboy joe"
print(name.title())

# Complete the following f-string print message 
    # You will need to create your own variables and insert them  
    # the final message should read `The University of Wyoming was founded in 1886`
Uname="university of wyoming"
year=1886 
print(f"The {Uname.title()} was founded in {year}")

# Now let's do some math with variables 
    # Create two variables x and y and assign them the values 5 and 10 respectively 
    # Complete the following print statements using your variables
    #All math must be done within the braces in the f-strings
x=5
y=10
print(f"x + y = {x+y}")
print(f"x - y = {x-y}")
print(f"x * y = {x*y}")
print(f"x / y = {x/y}")

# String concatenation 
    # Finally we will take a look at string concatenation
    # String concatenation combines two strings together
    # It is done using the + operator
    # Create three variables:
        # first_name, which is your first name 
        # last_name, which is your last name
        # space, which is a space character 
    # Use string concatenation to print out your full name 
first_name="marit"
last_name="mallberg"
space=" "
print(first_name+space+last_name)
  
#just for fun ... 
print(first_name.title()+space+last_name.title())
