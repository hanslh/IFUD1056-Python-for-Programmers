# Python for programmers Autumn 2017 - Assignment One by Hans Ludvig Holberg
# Python Version 3.5.4

# ***************************** Data Types *********************************

a = input("Type an integer value for a: ")
b = input("Type an integer value for b: ")
# Not converting the inputs to integer will cause python to interpret
# the operation c = a + b to be the appending of two strings, hence values
# of e.g. a = 2 and b = 3 will result in c = 23.
c = a + b
print("The sum of strings a + b = {}".format(c))

# Converting the values for a and b to integers before the summation gives
# the correct result where inputs of e.g. a = 2 and b = 3 produces c = 5
# given c = a + b.
c = int(a) + int(b)
print("The sum of integers a + b = {}".format(c))

# The expression below will create a TypeError because it is impossible to
# multiply two strings.
# print("The product of a * b = {}".format(a*b))

# Converting a and b to integers will make the expression work
print("The product of integers a * b = {}".format(int(a) * int(b)))

# Multiplying a string 'a' with an integer 'b' will print as 'a' appended
# to itself 'b' times
print("The product of string a * integer b = {}".format(a * int(b)))


# *************************** Text Formatting *******************************

# No separation between words
print("{0}{sep}{1}{sep}{2}{sep}{3}".format('Have', 'a', 'nice', 'day', sep=''))
# Words separated by a blank space
print("{0}{sep}{1}{sep}{2}{sep}{3}".format('Have', 'a', 'nice', 'day', sep=' '))
# Words separated by an arrow ->
print("{0}{sep}{1}{sep}{2}{sep}{3}".format('Have', 'a', 'nice', 'day', sep='->'))
# Words separated by a tap ^
print("{0}{sep}{1}{sep}{2}{sep}{3}".format('Have', 'a', 'nice', 'day', sep='^'))
# Words separated by return \n
print("{0}{sep}{1}{sep}{2}{sep}{3}".format('Have', 'a', 'nice', 'day', sep='\n'))
# Words separated by 5 blank lines _____
print("{0}{sep}{1}{sep}{2}{sep}{3}".format('Have', 'a', 'nice', 'day', sep='_____'))


# Block of 25 spaces with left adjusted text
print("{:25}".format('Have a nice day'))
# Block of 25 spaces with right adjusted text
print("{:>25}".format('Have a nice day'))
# Block of 25 spaces with right adjusted text and blank spaces filled with '*'
print("{:*>25}".format('Have a nice day'))
# Block of 25 spaces with left adjusted text and blank spaces filled with '*'
print("{:*<25}".format('Have a nice day'))
# Block of 25 spaces with centered text and blank spaces filled with '*'
print("{:*^25}".format('Have a nice day'))


# ***************************** Modulo Table *****************************

# Get input from user for the base value of the modulo multiplication table
baseX = input("Insert integer value for x to generate a modulo x multiplication table: ")
baseX = int(baseX)

# Print top line of a blank space followed by 'base' digits
# The end='' statement prevent the print function to generate newline after executing
print('   ', end='')
for x in range(baseX):
    print('{:3}'.format(x), end='')
# After all digits on first line are printed, manually move cursor to new line
print('\n')

# Calculate and print the remaining table
for y in range(baseX):
    # Starting with printing the base value for the new line
    print('{:3}'.format(y), end='')
    # followed by the calculated multiplication modulo for the respective line base value
    for z in range(baseX):
        print('{:3}'.format((y * z) % baseX), end='')
    print('\n')
