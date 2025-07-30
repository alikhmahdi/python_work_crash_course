from pathlib import Path


guest_file = Path("E:\\programming\\python\\books\\python crash course\\python_work_crash_course\\10_04_guest\\guest.txt")
guests = guest_file.read_text()
guest_file.write_text(guests + "\n" + input("Please enter the guest's name: "))
