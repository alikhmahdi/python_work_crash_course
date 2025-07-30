from pathlib import Path
import json


path = Path("E:\\programming\\python\\books\\python crash course\\python_work_crash_course\\10_13_user_dictionary\\user_dictionary.json")
try:
    users_info = json.loads(path.read_text())
except FileNotFoundError:
    users_info = {}


def quit_program(what):
    '''Ask the user if they want to quit the program.'''
    while True:
        quit = input(f"Do you want to {what}? (yes/no): ")
        if quit.lower() == "yes":
            end = True
            break
        elif quit.lower() == "no":
            end = False
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    return end


def dictionary_print(user_name, user_dict):
    '''Print the user dictionary in a readable format.'''
    print(f"{user_name}:")
    for what, reason in user_dict.items():
        print(f" - {what} : {reason}.")
def change_user_info(username):
    '''Change the user information in the users_info dictionary.'''
    while quit_program("change information"):
        what = input("Enter the information you want to change: ")
        if what in users_info[username]:
            users_info[username][what] = input(f"Enter your new {what}: ")
        elif what in users_info[username]["more_info"]:
            users_info[username]["more_info"][what] = input(f"Enter your new {what}: ")
        else:
            print(f"{what} not found in more_info.")
# Set the path to the JSON file
data = ["first name", "last name", "email", "phone number", "date of birth(yy/mm/dd)"]
while quit_program("use info program"):
    username = input("Enter your username: ")
    if username in users_info.keys():
        print("I remember your information:")
        dictionary_print(username, users_info[username])
    else:
        users_info[username] = {}
        for item in data:
            users_info[username][item] = input(f"Enter your {item}: ")
            users_info[username]["more_info"] = {}
        while quit_program("add more information"):
            what = input("Enter the information you want to add: ")
            users_info[username]["more_info"][what] = input(f"Enter your {what}: ")            
    change_user_info(username)
path.write_text(json.dumps(users_info))
