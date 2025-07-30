end = True
while True:
    quit = input("Do you want to use the calculator? (yes/no): ")
    if quit.lower() == "yes":
        break
    elif quit.lower() == "no":
        end = False
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        continue
while end:
    try:
        num1 , num2 = int(input("Enter two numbers:\n")), int(input())
    except ValueError:
        print("Invalid input. Please enter two numbers.")
    else:
        print("The sum is:", num1 + num2)
    while True:
        quit = input("Do you want to quit? (yes/no): ")
        if quit.lower() == "yes":
            end = False
            break
        elif quit.lower() == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue