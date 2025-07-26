import admin

class User:
    '''A class to represent a user.'''


    def __init__(self, first_name, last_name, age, location, email, admin_status=False):
        '''Initialize user attributes.'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.admin_status = admin.Admin(admin_status)

    def describe_user(self):
        '''Display user information.'''
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Email: {self.email}\n")
        self.admin_status.privileges.show_privileges()


    def greet_user(self):
        '''Simulate greeting the user.'''
        print(f"Hello, {self.first_name} {self.last_name}!")
        print(f"Welcome to our platform, {self.first_name}!\n")