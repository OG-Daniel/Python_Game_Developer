# abc = 123
# print(abc)


# Dictionaries are one of the data type available in python
# Dictionaries are represented using curly brackets
# Dictionary items are stored in the form of key and value
# All keys in the dictionary should be unique, values though can be same
# The values in a dictionary item can only be accessed through keys
# an item in a dictionary can be added by declaring key first and then the value


sample = {"name" : "Daniel", "Age" : 12, 371 : "Test"}
print(sample)


print(sample["Age"])

# Checking all keys in a dictionary
print(sample.keys())

# Checking all values in a dictionary
print(sample.values())

# Checking all items in a dictionaries
print(sample.items())

# Adding an item in a dictionary
sample["Profession"] = "Student"
print(sample)

# Deleting an item from a dictionary
del sample[371]
print(sample)
