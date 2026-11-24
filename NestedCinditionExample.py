'''if True:
    print("This is true")
    if True:
        print("This is also true")
        if True:
            print("This is also true 555")'''
            
usernameInput = input("Enter your username: ")
passwordInput = input("Enter your password: ")
if usernameInput == "admin" and passwordInput == "1234":
    print("Login successful!")
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    userSelect = int(input("Select your menu: "))
    if userSelect == 1: 
        price = float(input("Enter your price : (THB)"))
        vat = 7
        result = price + (price * vat/100)
        print("Price: ", price)
        print("VAT: ", vat)
        print("Total Price: ", result)
    elif userSelect == 2:
        price = float(input("Enter your first product price : (THB)"))
        price2 = float(input("Enter your second product price : (THB)"))
        totalPrice = price + price2
        print("Total Price: ", totalPrice)