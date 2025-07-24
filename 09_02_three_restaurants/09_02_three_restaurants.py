class Restaurant:
    '''A class to represent a restaurant.'''

    
    def __init__(self, restaurant_name, cuisine_type):
        '''Initialize restaurant name and cuisine type.'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        '''Display restaurant information.'''
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")


    def open_restaurant(self):
        '''Simulate opening the restaurant.'''
        print(f"{self.restaurant_name} is now open!")


restaurant1 = Restaurant(restaurant_name="McDonald's", cuisine_type="Fast Food")
restaurant2 = Restaurant(restaurant_name="Olive Garden", cuisine_type="Italian")
restaurant3 = Restaurant(restaurant_name="Taco Bell", cuisine_type="Mexican")

print("\nDescribing restaurants:")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
