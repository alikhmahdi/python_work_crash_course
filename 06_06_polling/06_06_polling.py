people = ['alice', 'bob', 'charlie', 'mahdi', 'jalal']
favorite_languages = {
    'alice': 'ruby',
    'bob': 'java',
    'jalal': 'python'
}

print("Poll results:")
for name in sorted(people):
    message = favorite_languages.get(name, 'Take the poll!\n   or Get the fuck out!')
    print(f"- {name.title()}: {message}")
