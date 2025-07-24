favorite_places = {
    'Alice': ['Paris', 'London', 'Rome'],
    'Bob': ['New York', 'Los Angeles', 'Chicago'],
    'Charlie': ['Tokyo', 'Sydney', 'Melbourne']
}
for name, places in favorite_places.items():
    print(f"{name}'s favorite places are:")
    for place in places:
        print(f" - {place}")