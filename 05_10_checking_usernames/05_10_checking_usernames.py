current_users = ['alice', 'bob', 'mahtaa','charlie']
new_users = ['alice', 'eva', 'Frank','JON','MAhtaa',"Eva"]
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"User '{new_user}' is already taken.\nPlease choose a different username.\n\n")
    else:
        print(f"User '{new_user}' is available.\n\n")
        current_users.append(new_user.lower())
print(f"Updated list of users: {current_users}\n\n")
