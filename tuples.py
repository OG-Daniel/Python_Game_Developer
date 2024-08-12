# Tuples are another kind of data structures in python and are represented using round brackets
# Tupleas follow indexing, slicing concepts just like lists
# Tuples are immutable.  Once a tuple has been generated, it cannot be modified or altered
# Tuples follow the concept of unpacking where we can extract all the sub values inside a tuple
# Tuple can comntain data like integers, floats, string, lists, boolean and tuple as well


abc = (13, 86.12, "Tuples", True, ["test", "Hello World", 999], ("test", "Hello World", 999))

# Unpacking concept -- Hee we can pass separate variable names in order to extract all the values inside a tuple

int1, float1, str1, bool1, list1, tup1 = abc

print("Integer inside tuple is : ", int1)
print("Tuple inside tuple is : ", tup1)


## Indexing concept

print(abc[2])
print(abc[-2])
print(abc[2][3])
print(abc[4][1][3])


## Slicing

print(abc[0:3])

print(abc[2 : ])