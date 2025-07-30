from pathlib import Path
path =  Path("E:\\programming\\python\\books\\python crash course\\python_work_crash_course\\10_10_common_words\\Ifcarpenters_were_hired_like_programmers.txt")
text = path.read_text()
count_words = len(text.split())
print(f'Number of words: {count_words}')
print(f'Number of "but": {text.count("but")}')
print(f'Number of "but", "But", etc : {text.lower().count("but")}')