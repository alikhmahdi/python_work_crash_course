print("Hello and welcome to our restaurant!")
toppings = []
topping = ''
topping = input("Please enter a pizza topping (or 'quit' to finish): ")
while topping.lower() != 'quit':
    toppings.append(topping)
    print(f"We added '{topping}' to your pizza.")
    topping = input("Please enter a pizza topping (or 'quit' to finish): ")
if len(toppings) == 0:
    print("No toppings were selected.")
else:
    print("\n\nHere are the toppings you selected:")
    for topping in toppings:
        print("- " + topping)