from pathlib import Path


guest_file = Path("E:\\programming\\python\\books\\python crash course\\python_work_crash_course\\10_05_guest_book\\guest_book.txt")
new_file = input("Do you want to create a new guest book file? (yes/no) ")
while True:
    if new_file.lower() == "yes":
        try:
            guests = guest_file.read_text()
        except FileNotFoundError:
            guests = ""
        break
    elif new_file.lower() == "no":
        guests = ""
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        new_file = input("Do you want to create a new guest book file? (yes/no) ")
print("Please enter the guest's name (or 'q' to quit):")
while True:
    guest_name = input()
    if guest_name.lower() == 'q':
        break
    if guest_name:
        guests += guest_name + "\n"
guest_file.write_text(guests)
