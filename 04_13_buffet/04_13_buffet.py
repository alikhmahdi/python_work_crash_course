menu = ('pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream')
print("The buffet menu includes:")
for food in menu:
    print(f" - {food}")
# menu[0]='sushi'
menu = ('sushi','hamburger') + menu[2:]
print("The new buffet menu includes:")
for food in menu:
    print(f" - {food}")