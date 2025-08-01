import city_functions


def test_city_country():
    '''Test the city_country() function.'''
    formatted_name = city_functions.city_country('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'
    formatted_name = city_functions.city_country('tehran', 'iran')
    assert formatted_name == 'Tehran, Iran'


def test_city_country_population():
    '''Test the city_country_population() function.'''
    formatted_name = city_functions.city_country_population('santiago', 'chile', 5000000)
    assert formatted_name == 'Santiago, Chile - Population = 5000000'
    formatted_name = city_functions.city_country_population('tehran', 'iran', 9000000)
    assert formatted_name == 'Tehran, Iran - Population = 9000000'