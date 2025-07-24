def make_car(manufacturer, model, **car):
    '''Build a dictionary representing a car with the given manufacturer, model, and any details.'''
    car['manufacturer'] = manufacturer
    car['model'] = model
    return car
print(make_car('subaru', 'outback', color='blue', tow_package=True))
print(make_car('honda', 'i8', color='black', sunroof=True, interior_color='red'))
print(make_car('honda', 'i8', color='blue'))