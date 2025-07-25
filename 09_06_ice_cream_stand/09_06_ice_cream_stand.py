class IceCreamStand():
    '''A class to represent an ice cream stand.'''


    def __init__(self, *flavors):
        '''Initialize ice cream stand attributes.'''
        self.flavors = set(flavors)


    def add_flavor(self, flavor):
        '''Add a new ice cream flavor.'''
        self.flavors.add(flavor)
        print(f"Added new flavor: {flavor}")


    def remove_flavor(self, flavor):
        '''Remove an ice cream flavor.'''
        self.flavors.discard(flavor)
        print(f"Removed flavor: {flavor}")


    def display_flavors(self):
        '''Display the available ice cream flavors.'''
        print("Available Ice Cream Flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")


class Restaurant:
    '''A class to represent a restaurant.'''

    
    def __init__(self, restaurant_name, cuisine_type,*flavors):
        '''Initialize restaurant name and cuisine type.'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.ice_cream_stand = IceCreamStand(*flavors)


    def describe_restaurant(self):
        '''Display restaurant information.'''
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")


    def open_restaurant(self):
        '''Simulate opening the restaurant.'''
        print(f"{self.restaurant_name} is now open!")


    def set_number_served(self, number):
        '''Set the number of customers served.'''
        self.number_served = number


    def increment_number_served(self, increment=1):
        '''Increment the number of customers served.'''
        if increment > 0:
            self.number_served += increment


franklin_fountain = Restaurant("Franklin Fountain", "American", "Banana")
franklin_fountain.ice_cream_stand.display_flavors()
franklin_fountain.ice_cream_stand.add_flavor("Vanilla")
franklin_fountain.ice_cream_stand.add_flavor("Chocolate")
franklin_fountain.ice_cream_stand.add_flavor("Strawberry")
franklin_fountain.ice_cream_stand.display_flavors()
franklin_fountain.ice_cream_stand.remove_flavor("Chocolate")
franklin_fountain.ice_cream_stand.display_flavors()