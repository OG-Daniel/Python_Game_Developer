userchoice = input("Enter a statement: ")
alphabet = "abcd"

def panagram(str):
    for i in alphabet:
        if i not in str.lower():
            return False
    return True


if panagram(userchoice) == True:
    print ("Yes, It is a panagram statement.")
else:
    print ("No, It is not a panagram statement.")
    