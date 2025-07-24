def make_shirt(size, text):
    '''Make a T-shirt with the given size and text.'''
    print(f"We gone make you a {size} T-shirt with this massage:\n - {text}")
size_input, text_input = input('What should the size of T-shirt be? '), input('What do you want to rowet on it? ')
make_shirt(size_input, text_input)
make_shirt(text=text_input, size=size_input)