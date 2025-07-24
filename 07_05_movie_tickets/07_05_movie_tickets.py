age = input("Please enter your age (or 'quit' to finish): ")
while age.lower() != 'quit':
    if age.isdigit():
        age = int(age)
        if age < 3:
            print("Your ticket is free!(You're our guest!)")
        elif age < 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")
    else:
        print("Invalid input. Please enter a valid age.")
    age = input("Please enter your age (or 'quit' to finish): ")