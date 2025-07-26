import admin

mahdi = admin.User("Mahdi", "Doe", 30, "New York", "mahdi@example.com")
mahdi.describe_user()
print('\n')
mahdi.greet_user()

mo = admin.User("Mohammad", "Smith", 28, "Los Angeles", "mo@example.com", admin_status=True)
mo.describe_user()
print('\n')
mo.greet_user()
