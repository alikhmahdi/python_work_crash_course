class User:
    '''A class to represent a user.'''


    def __init__(self, first_name, last_name, age, location, email):
        '''Initialize user attributes.'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email


    def describe_user(self):
        '''Display user information.'''
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Email: {self.email}\n\n")


    def greet_user(self):
        '''Simulate greeting the user.'''
        print(f"Hello, {self.first_name} {self.last_name}!")
        print(f"Welcome to our platform, {self.first_name}!")


user1 = User("Alice", "Smith", 30, "New York", "alice@example.com")
user2 = User("Bob", "Johnson", 25, "Los Angeles", "bob@example.com")
user3 = User("Charlie", "Williams", 35, "Chicago", "charlie@example.com")

print("Describing users:")
user1.describe_user()
user2.describe_user()
user3.describe_user()

print("Greeting users:")
user1.greet_user()
user2.greet_user()
user3.greet_user()
