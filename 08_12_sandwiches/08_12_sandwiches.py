def sandwich_topping(size, *toppings):
    '''Display a topping for a sandwich.'''
    print(f"Making a {size}cm sandwich with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")
sandwich_topping(10, "lettuce", "tomato", "turkey")
sandwich_topping(15, "ham")
sandwich_topping(12, "cheese", "pickles")

