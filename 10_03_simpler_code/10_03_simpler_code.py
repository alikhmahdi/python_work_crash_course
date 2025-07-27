from pathlib import Path


# Define the path to the directory you want to explore
path = Path('E:\\programming\\python\\books\\python crash course\\python_work_crash_course\\10_01_learning_python\\learning_python.txt')

# Print whole content by read_text method
print('whole:')
print(path.read_text())
# adding lines to variable one by one
lines = []
for line in path.read_text().splitlines():
	lines.append(line)
print(lines)
