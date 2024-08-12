# Program to generate list of numbers and print squares of odd and even separately

odd_squares = []
even_squares = []

start = int(input("Enter the starting range:  "))
end = int(input("Enter the ending range:  "))

for i in range (start, end+1):
    if i %2 == 0:
        even_squares.append(i ** 2)
    else:
        odd_squares.append(i ** 2)

print("The even squares are: ", even_squares)
print("The odd squares are: ", odd_squares)
    
