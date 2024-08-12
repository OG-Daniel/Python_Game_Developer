# Vowels= {}
# vowels = "a" "e" "i" "o" "u"

  
# animal = input("Enter an animal: ").lower()
# child = input("Enter an animal child: ").lower()
# Vowels[animal] = child

# animal.split()
# animal.count(vowels)
# print (animal)

userchoice = input("Enter a sentence: ")
vowels = {"a" : 0, "e" : 0, "i" : 0,  "o" : 0, "u" : 0} 

for i in userchoice: 
    if i in vowels:
        vowels [i] += 1

print (vowels)