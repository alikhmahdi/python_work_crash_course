cities = {
    'tehran': {
        'country': 'Iran',
        'population': 9000000,
        'fact': 'Tehran is the capital of Iran.'
    },
    'paris': {
        'country': 'France',
        'population': 2148000,
        'fact': 'Paris is known as the city of love.'
    },
    'tokyo': {
        'country': 'Japan',
        'population': 13960000,
        'fact': 'Tokyo is the most populous city in the world.'
    }
}

for city, info in cities.items():
    print(f"\nSome information about {city.title()}:")
    for key, value in info.items():
        print(f" - {key.title()}: {value}")