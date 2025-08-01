def city_country(city: str, country: str) -> str:
    '''Return a neatly formatted city and country pair.'''
    return f"{city.title()}, {country.title()}"


def city_country_population(city: str, country: str, population: int) -> str:
    '''Return a neatly formatted city, country, and population pair.'''
    return f"{city.title()}, {country.title()} - Population = {population}"