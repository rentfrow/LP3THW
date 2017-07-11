# assigning a digit to a variable
types_of_people = 10

# assiging a string to a variable while inserting a 
# variable value inside the string using "format string"
x = f"There are {types_of_people} types of people."

# assigning a strings to 2 variables
binary = "binary"
do_not = "don't"
# assiging a string to a variable while inserting the
# two variable strings inside the string using "format string"
y = f"Those who know {binary} and those who {do_not}."

# printing the two variable strings
print(x)
print(y)

# printing two strings while printing two variable strings
# inside the strings using "format string"
print(f"I said: {x}")
print(f"I also said: {y}")

# Assigning a variable the boolean value "False"
hilarious = True

# Creating a variable with placeholder "{}" for .format() syntax
joke_evaluation = "Isn't that joke so funny?! {}"

# Printing a variable while inserting another variable using .format() syntax
print(joke_evaluation.format(hilarious))

# Assigning strings to two variables
w = "This is the left side of..."
e = "a string with a right side."

# Printing and concating the two strings together
print(w + e)
