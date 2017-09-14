# Python for programmers Autumn 2017 - Assignment Two by Hans Ludvig Holberg
# Developed on Python Version 3.5.4

# The algorithms below compare two strings of different length and identify any unique characters for each string. The difference
# between the algorithms is their processing complexity due to how they are implemented. A good approximation for calculating
# the complexity of an algorithm can be to count how many assignment (=) operations it includes. This again is used to find the "Big-O
# Notation" which is a generic way of specifying the complexity of an algorithm. Experimental results to back up the theory can be gained
# by measuring the processing time for each algorithm. However processing time is only good for relative performance comparison between
# algorithms running on the same system. This is because the absolute processing times are higly dependant of avalaible processing power
# in addition to the algorithm complexity itself. Differences of processing time between the algorithms is difficult to see clearly without
# running large strings through the programme.

# Prerequisite: The algorithms only handle small letters between a-z. All other letters will make the programme crash.

# Time library required for processing time measurements
import time


# ****************** O(n^2) Solution - Checking Off ************************

def checkingOff(s1, s2):
    print("Running the Checking Off O(n^2) algorithm...")

    # Get timestamp for start of algorithm
    startTime = time.time()

    # Create list from s2 to get immutable access - O(1)
    list2 = list(s2)

    # Flags to indicate if all characters in one string are present in the other- O(1)
    charMatchString1 = True
    charMatchString2 = True

    # The nested loop below starts with first character in s1 and compares it to each character in s2
    # until a match is found or the end of s2 is reached - O(n^2)
    # Outer loop run until reaching end of s1
    pos1 = 0
    while pos1 < len(s1):

        # Support flag indicating that a match has been found
        found = False

        # Inner loop increments position counter for s2. Runs until reaching end of s2
        pos2 = 0
        while pos2 < len(list2) and not found:
            if s1[pos1] == list2[pos2]:
                # If a match is found, the inner loops stops and the found flag is set
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            # When a character match is found, the character position in s2 is overwritten with 'None' to
            # prevent the algorithm to match the same character twice.
            list2[pos2] = None
        else:
            # If the character from string1 is not found, this character is printed and the flag indicating that
            # not all characters in string1 are present in string2 is set
            print("The character '" + s1[pos1] + "' is not present in string 2")
            charMatchString1 = False

        # Move to next character in string1
        pos1 = pos1 + 1

    # After the nested loop has finished, check string2 for any characters not set to 'None'. These are characters
    # not present in string1 and is printed as such.
    pos2 = 0
    while pos2 < len(list2):
        if list2[pos2] != None:
            print("The character '" + list2[pos2] + "' is not present in string 1")
            charMatchString2 = False
            pos2 = pos2 + 1
        else:
            pos2 = pos2 + 1

    # Print conclusion based on status of character match flags
    if charMatchString1 and charMatchString2:
        print("String 1 and string 2 are identical")
    elif charMatchString1:
        print("All characters in string 1 are present in string 2")
    elif charMatchString2:
        print("All characters in string 2 are present in string 1")
    else:
        print("String 1 and string 2 both have unique characters")

    # Get timestamp for end of algorithm and print processing time
    endTime = time.time()
    print("Processing time: " + str(endTime - startTime) + "s")


# *************** O(n log n) Solution - Sort and Compare *******************

def sortCompare(s1, s2):
    print("Running the Sort and Compare O(n log n) algorithm...")

    # Get timestamp for start of algorithm
    startTime = time.time()

    # Convert strings to lists to create mutable access - O(1)
    list1 = list(s1)
    list2 = list(s2)

    # Worst case performance of python's sort-function (Timsort) is O(n log n) ref. "en.wikipedia.org/wiki/Timsort"
    list1.sort()
    list2.sort()

    # Assigning support variables - O(1)

    # Position counters for each of the lists
    pos1 = 0
    pos2 = 0
    # Flags to indicate if all characters in one string are present in the other.
    charMatchString1 = True
    charMatchString2 = True

    # Scanning through the lists once and comparing character for character - O(n)
    # Run the loop till both position counters has reached the end of its respective string
    while pos1 != len(list1) or pos2 != len(list2):

        # if reached end of list 1
        if pos1 == len(list1):
            # print the remaining characters in list 2 as unique
            while pos2 < len(list2):
                print("The character '" + list2[pos2] + "' is not present in string 1")
                pos2 = pos2 + 1
                charMatchString2 = False

        # if reached end of list 2
        elif pos2 == len(list2):
            # print the remaining characters in list 1 as unique
            while pos1 < len(list1):
                print("The character '" + list1[pos1] + "' is not present in string 2")
                pos1 = pos1 + 1
                charMatchString1 = False

        # If the sorted characters match up
        elif list1[pos1] == list2[pos2]:
            # proceed to next character in both strings
            pos1 = pos1 + 1
            pos2 = pos2 + 1

        # If the characters does not match up
        else:
            # Identify which string contains the character with lowest sort order -> Character is not present in the other string
            # The comparison expression below works because the ascii value for characters are sequenced in alphabetical order

            # Lowest character is in string1
            if list1[pos1] < list2[pos2]:
                # Print lower order character and increment only the position for the string containing the character
                print("The character '" + list1[pos1] + "' is not present in string 2")
                # Set flag that this string contain a character not present in the other string
                charMatchString1 = False
                pos1 = pos1 + 1

            # Lowest character is in string2
            else:
                # The same process as above for string1
                print("The character '" + list2[pos2] + "' is not present in string 1")
                charMatchString2 = False
                pos2 = pos2 + 1

    # Print conclusion based on status of character match flags
    if charMatchString1 and charMatchString2:
        print("String 1 and string 2 are identical")
    elif charMatchString1:
        print("All characters in string 1 are present in string 2")
    elif charMatchString2:
        print("All characters in string 2 are present in string 1")
    else:
        print("String 1 and string 2 both have unique characters")

    # Get timestamp for end of algorithm and print processing time
    endTime = time.time()
    print("Processing time: " + str(endTime - startTime) + "s")

    # I am not surprised if there is a more refined solution for this algorithm, but I'm not able to find it.

# ****************** O(n) Solution - Count and Compare *********************

# The first part of this algorithm is more or less a copy of the algorithm presented as Solution 4 in
# the lecture material


def countCompare(s1, s2):
    print("Running the Count and Compare O(n) algorithm...")

    # Get timestamp for start of algorithm
    startTime = time.time()

    # Construct a list for each string with a length of 26 (alphabet) which are initilized to '0' - O(1)
    c1 = [0] * 26
    c2 = [0] * 26

    # Flags to indicate if all characters in one string are present in the other.
    charMatchString1 = True
    charMatchString2 = True

    # Count occurences of characters in string 1 - O(n)
    for i in range(len(s1)):
        # Subtracting the ascii value for 'a' from the characters in the string gives 'a' the numeric
        # value of 0 and 'z' the numeric value of 25. This means c1[0] contains the number of 'a's in the
        # string, c1[1] contain number of 'b's and so on. The ord() function returns the unicode of its
        # argument character
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1

    # Count occurences of characters in string 2 - O(n)
    for i in range(len(s2)):
        # Repeat same process as above for string 2
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1

    # Compare occurences of each letter in both strings - O(n)
    for i in range(25):
        # If fewer occurence of a character in string 1 than string 2
        if c1[i] < c2[i]:
            charMatchString2 = False

            # Print all extra occurences of the character in string 2 that is not present i string 1
            j = c2[i] - c1[i]
            while j != 0:
                # Convert the list index back to its respective character using the chr() function
                print("The character '" + chr(i + ord('a')) + "' is not present in string 1")
                j = j - 1

        elif c1[i] > c2[i]:
            charMatchString1 = False

            # Print all extra occurences of the character in string 2 that is not present i string 1
            j = c1[i] - c2[i]
            while j != 0:
                # Convert the list index back to its respective character using the chr() function
                print("The character '" + chr(i + ord('a')) + "' is not present in string 2")
                j = j - 1

    # Print conclusion based on status of character match flags
    if charMatchString1 and charMatchString2:
        print("String 1 and string 2 are identical")
    elif charMatchString1:
        print("All characters in string 1 are present in string 2")
    elif charMatchString2:
        print("All characters in string 2 are present in string 1")
    else:
        print("String 1 and string 2 both have unique characters")

    # Get timestamp for end of algorithm and print processing time
    endTime = time.time()
    print("Processing time: " + str(endTime - startTime) + "s")


# ***************************************************************************
#                                 Main
# ***************************************************************************

# Get input from user
print("This program compares characters of two strings using algorithms of different complexity.")
s1 = input("Insert string 1: ")
s2 = input("Insert string 2: ")

print("\n")

# Call function for Checking Off - O(n^2)
checkingOff(s1, s2)

print("\n")

# Call function for Sort And Compare Algorithm - O(n log n)
sortCompare(s1, s2)

print("\n")

# Call function for Count And Compare Algorithm - O(n)
countCompare(s1, s2)
