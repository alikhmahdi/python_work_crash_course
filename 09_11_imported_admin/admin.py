class Privileges:
    '''A class to represent the privileges of a user.'''

    def __init__(self, admin_status):
        '''Initialize privileges attributes.'''
        if admin_status:
            self.privileges = ["can add post", "can delete post", "can ban user"]
        else:
            self.privileges = [None]

    def show_privileges(self):
        '''Display the user's privileges.'''
        print("\nUser Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin():
    '''A class to represent an admin user.'''


    def __init__(self, admin_status):
        '''Initialize admin attributes.'''
        self.privileges = Privileges(admin_status)


class User:
    '''A class to represent a user.'''


    def __init__(self, first_name, last_name, age, location, email, admin_status=False):
        '''Initialize user attributes.'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.admin_status = Admin(admin_status)

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