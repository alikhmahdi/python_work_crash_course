profit, people = 0, 0
while True:
    age = input("Please enter your age (or 'quit' to finish): ")
    if age.lower() == 'quit':
        break
    if not age.isdigit():
        print("Invalid input. Please enter a valid age.")
        continue
    age = int(age)
    people += 1
    if age < 3:
        print("Your ticket is free!(You're our guest!)")
    elif age < 12:
        print("Your ticket is $10.")
        profit += 10
    else:
        print("Your ticket is $15.")
        profit += 15
print(f"We earn ${profit} from {people} people.")