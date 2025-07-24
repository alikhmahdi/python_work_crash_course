class Restaurant:
    '''A class to represent a restaurant.'''

    
    def __init__(self, restaurant_name, cuisine_type):
        '''Initialize restaurant name and cuisine type.'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


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

print("Creating restaurant instances McDonald's Fast Food:")
mcdonalds = Restaurant(restaurant_name="McDonald's", cuisine_type="Fast Food")
mcdonalds.describe_restaurant()
mcdonalds.open_restaurant()
mcdonalds.set_number_served(100)
print(f"Number of customers served before increment: {mcdonalds.number_served}")
mcdonalds.increment_number_served(50)
print(f"Number of customers served after increment: {mcdonalds.number_served}")
