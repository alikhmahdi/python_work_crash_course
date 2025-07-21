rivers = {
    'nile': 'Egypt',
    'amazon': 'South America',
    'yangtze': 'China',
    'mississippi': 'United States',
    'danube': 'Central and Eastern Europe',
}


print("Rivers and their countries:")
for river, country in sorted(rivers.items()):
    print(f"- The {river.title()} flows through {country}.\n")


print("Rivers:")
for river in sorted(rivers.keys()):
    print(f"- The {river.title()}\n")


print("Countries:")
for country in sorted(rivers.values()):
    print(f"- The {country.title()}.\n")