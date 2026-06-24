try:
    val1 = int(input("Enter the first number:"))
    val2 = int(input("Enter the second number: "))
    print("What kind of operation do you want to perform?.\nPress + for addition.\nPress - for substraction. \nPress * for multiplication.\n Press / for division.")

    O = input("Enter your operation: ") 

    match O:
        case "+":
            print(f"the result is {val1 + val2}")

        case"-":
            print(f"The result is {val1 - val2}")

        case"*":
            print(f"The result is {val1 * val2}")

        case "/":
            print(f"The result is {val1 / val2}")

        case default:
            print("invalid inputs")

except ValueError as e:
    print("Invalid input.Please enter a valid number.")

