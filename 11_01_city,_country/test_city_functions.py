from city_functions import city_country


def test_city_country():
    '''Test the city_country() function.'''
    formatted_name = city_country('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'