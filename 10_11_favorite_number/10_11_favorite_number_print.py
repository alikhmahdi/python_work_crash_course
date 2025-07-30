from pathlib import Path
import json


# Set the path to the JSON file
path = Path("E:\\programming\\python\\books\\python crash course\\python_work_crash_course\\10_11_favorite_number\\favorite_number.json")
try:
    users_favorite_numbers = json.loads(path.read_text())
except FileNotFoundError:
    print("No favorite user's numbers found.")
else:
    if users_favorite_numbers:
        print("Favorite user's numbers:")
        for name, number in users_favorite_numbers.items():
            print(f" - {name}: {number}")
    else:
        print("No favorite user's numbers found.")