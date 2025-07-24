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

print("Creating restaurant instances McDonald's Fast Food:")
mcdonalds = Restaurant(restaurant_name="McDonald's", cuisine_type="Fast Food")
mcdonalds.describe_restaurant()
mcdonalds.open_restaurant()
