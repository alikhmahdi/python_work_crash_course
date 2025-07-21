logined_users = ['alice', 'bob', 'admin','charlie']
for user in logined_users:
    if user == 'admin':
        print("Hello Admin,\n Would you like to see a status report?")
    else:
        print(f"Hello {user.title()},\n Thank you for logging in again.")
