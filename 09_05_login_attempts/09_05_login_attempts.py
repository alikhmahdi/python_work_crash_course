class User:
    '''A class to represent a user.'''


    def __init__(self, first_name, last_name, age, location, email):
        '''Initialize user attributes.'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.login_attempts = 0


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


    def increment_login_attempts(self):
        '''Increment the login attempts.'''
        self.login_attempts += 1


    def reset_login_attempts(self):
        '''Reset the login attempts.'''
        self.login_attempts = 0


user1 = User("Alice", "Smith", 30, "New York", "alice@example.com")


print("Describing users:")
user1.describe_user()

print("Greeting users:")
user1.greet_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"Login attempts: {user1.login_attempts}")
user1.reset_login_attempts()
print(f"Login attempts after reset: {user1.login_attempts}")
user1.increment_login_attempts()
print(f"Login attempts after increment again: {user1.login_attempts}")