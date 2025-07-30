from pathlib import Path
import json


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


# Set the path to the JSON file
path = Path("E:\\programming\\python\\books\\python crash course\\python_work_crash_course\\10_12_favorite_number_remembered\\favorite_number.json")
try:
    users_favorite_numbers = json.loads(path.read_text())
except FileNotFoundError:
    users_favorite_numbers = {}
while quit_program("use the favorite number"):
    name = input("Enter your name: ")
    if name in users_favorite_numbers:
        print(f"Hello {name}, I remember your favorite number(It is {users_favorite_numbers[name]}).")
        if quit_program("change favorite number"):
            while True:
                try:
                    favorite_number = int(input("Enter your favorite number: "))
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    break
                else:
                    users_favorite_numbers[name] = favorite_number
                    break
    else:
        try:
            favorite_number = int(input("Enter your favorite number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        else:
            users_favorite_numbers[name] = favorite_number
path.write_text(json.dumps(users_favorite_numbers))