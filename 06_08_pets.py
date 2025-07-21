pets = [
    {'name': 'Buddy', 'species': 'Dog', 'age': 5, 'owner': 'Alice'},
    {'name': 'Mittens', 'species': 'Cat', 'age': 3, 'owner': 'Bob'},
    {'name': 'Goldie', 'species': 'Fish', 'age': 1, 'owner': 'Charlie'}
]
for pet in pets:
    print(f"{pet['name']} is a {pet['age']} year old {pet['species']} owned by {pet['owner']}.")