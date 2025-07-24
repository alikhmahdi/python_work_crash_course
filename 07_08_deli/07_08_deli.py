sandwich_orders = ["tuna", "club", "veggie", "club"]
finished_sandwiches = []

while sandwich_orders:
    order=input(f'You can chose between {sandwich_orders}. What sandwich would you like? ')
    if order.lower() not in sandwich_orders:
        print("Sorry, we don't have that sandwich.")
        continue
    sandwich_orders.remove(order.lower())
    finished_sandwiches.append(order.lower())
    print(f"I made your {order.lower()} sandwich.")

print("\nAll sandwiches made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
