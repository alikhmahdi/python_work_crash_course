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


class Admin:
    '''A class to represent an admin user.'''


    def __init__(self, admin_status):
        '''Initialize admin attributes.'''
        self.privileges = Privileges(admin_status)


