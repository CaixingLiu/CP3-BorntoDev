usernameInput = input("Enter your username: ")
passwordInput = input("Enter your password: ")
if usernameInput == "admin" and passwordInput == "1234":
    print("Login successful!")
    print("----- iShopee -----")
    print("1. Water 1 bottle 20 THB")
    print("2. Coke 1 box 25 THB")
    print("3. Milk 1 bottle 30 THB")
    print("4. noodles 1 cup 35 THB")
    userSelect = int(input("Select your Item: "))
    if userSelect == 1:
        price = 20
        k = int(input("How many bottles do you want to buy? "))
        print("Price: ", price)
        print("Quantity: ", k)
        print("Total Price: ", price * k)
    elif userSelect == 2:
        price = 25
        k = int(input("How many boxes do you want to buy? "))
        print("Price: ", price)
        print("Quantity: ", k)
        print("Total Price: ", price * k)
    elif userSelect == 3:
        price = 30
        k = int(input("How many bottles do you want to buy? "))
        print("Price: ", price)
        print("Quantity: ", k)
        print("Total Price: ", price * k)
    elif userSelect == 4:
        price = 35
        k = int(input("How many cups do you want to buy? "))
        print("Price: ", price)
        print("Quantity: ", k)
        print("Total Price: ", price * k)