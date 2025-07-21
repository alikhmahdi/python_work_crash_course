people = [
    {'name': 'Alice','last_name': 'Smith', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'last_name': 'Johnson', 'age': 25, 'city': 'Los Angeles'},
    {'name': 'Charlie', 'last_name': 'Williams', 'age': 35, 'city': 'Chicago'}
]
for person in people:
    print(f"{person['name']} {person['last_name']} is {person['age']} years old and lives in {person['city']}.")