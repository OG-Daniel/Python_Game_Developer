CountryDB= {}

while True:
    print("1. Insert")
    print("2. Display all countries")
    print("3. Display all capitals")
    print("4. Get capital")
    print("5. Delete")

    #get user choice
    choice = int(input("Enter your Choice: "))

    if choice == 1: 
        country = input("Enter a country: ").lower()
        capital = input("Enter a capital: ").lower()
        CountryDB[country] = capital

    elif choice == 2: 
        print(list(CountryDB.keys()))
        
    elif choice == 3: 
        print(list(CountryDB.values()))

    elif choice == 4:
        country = input("Enter a country: ").lower()
        print(CountryDB.get(country))

    elif choice == 5:
        country = input("Enter a country that you want to delete: ").lower()
        del CountryDB[country]
    
    else:
        print("Invalid Input ")