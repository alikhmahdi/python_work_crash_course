my_pizzas = ['pepperoni', 'margherita', 'hawaiian']
friend_pizzas = my_pizzas[:]
my_pizzas.append('meat feast')
friend_pizzas.append('seafood')
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(f"- {pizza}")
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")