import random

list_1 = []
list_2 = []
list_3 = []

num = 20
start = 0
end = 100

random_numbers = random.sample(range(1, 101), 20)
#print(random_numbers)

for i in random_numbers:
    if i <=30:
        list_1.append(i)
    elif (30 < i < 70):
        list_2.append(i)
    else:
        list_3.append(i)

print("The failed student marks are: ", list_1)
print("The average student marks are: ", list_2)
print("The excellent student marks are: ", list_3)

# for i in range(20):
#     number = random.randint(0, 100)
# list_1 = []
# if number <= 30:
#     list_1.append(number)


# list_2 = []
# elif number >=31 and 69:
#     list_2.append(number)

#     list_3: []
# else:
#     list_3.append(number)
