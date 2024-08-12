### LISTS ###
# Lists are another kind of data type in python. Lists are represented using square brackets
# Lists can store different kinds of data in them Eg : Integers, Floats, Strings, Tuples, Dictionaries, Boolean and Lists itself
# Lists declared within a list are called as nested list
# Lists have the property of indexing and slicing
# Indexing is the property using which all the lists item are assigned a unique positional value. Indexes always start from 0 and go on like 0, 1, 2 ...
# Slicing is the property using which we would be extracting a portion of the list by passing respective index positions


abc = [12, 94.31, "Test Value", True, ["Hello World", 369, 14.76, False, True, ("Testing Again", 718)]]
#print(abc)

# Length of a list
print(len(abc))

# Data type
print(type(abc))

## Indexing
# Indexes are of two types : Positive and Negative Index
# Positive indexes are in the direction from left to right. Positive indexes values are 0, 1, 2 ... 
# Negative indexes are in the direction from right to left. Negative index values are -1, -2, -3, ...

abc = [12, 94.31, "Test Value", True, ["Hello World", 369, 14.76, False, True, ("Testing Again", 718)]]

print(abc[2])
print(abc[4])

print(abc[2][7])
print(abc[4][2])

print(abc[4][0][3])
print(abc[4][5][1])
print(abc[4][5][0][3])

print(len(abc[4]))