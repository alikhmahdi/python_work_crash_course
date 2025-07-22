sandwich_orders = ["pastrami", "tuna", "pastrami", "club", "veggie", "club", "pastrami"]
print(f'We can make {sandwich_orders.count("pastrami")} Pastrami sandwiches so I delete it from the list.')
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print("No more pastrami sandwiches available.")
print(f'We can make {sandwich_orders} sandwiches now.')