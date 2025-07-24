def describe_city(city, country = 'Iran'):
    '''Describe the city and its country.'''
    print(f'{city.title()} is in the {country.title()}')
describe_city(city='tehran')
describe_city(city='londen',country='england')
describe_city(city='shiraz',country='Iran')