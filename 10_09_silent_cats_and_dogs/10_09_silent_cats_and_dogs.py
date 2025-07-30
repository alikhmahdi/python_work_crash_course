from pathlib import Path 


# add your own path
path_dogs = Path("E:\\programming\\python\\books\\python crash course\\python_work_crash_course\\10_08_cats_and_dogs\\dogs.txt")
path_cats = Path("E:\\programming\\python\\books\\python crash course\\python_work_crash_course\\10_08_cats_and_dogs\\cats.txt")
try:
    lines_dogs = path_dogs.read_text()
except FileNotFoundError:
    pass
else:
    print("Dogs:")
    for line in lines_dogs.splitlines():
        print("-", line)


try:
    lines_cats = path_cats.read_text()
except FileNotFoundError:
    pass
else:
    print("Cats:")
    for line in lines_cats.splitlines():
        print("-", line)