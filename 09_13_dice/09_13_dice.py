import random 


class Die:
    '''A class to represent a die.'''


    def __init__(self, sides=6):
        '''Initialize the die's attributes.'''
        self.sides = sides


    def roll(self):
        '''Simulate rolling the die.'''
        return random.randint(1, self.sides)


for _ in range(10):
    die = Die()
    print(f"Rolling a {die.sides}-sided die: {die.roll()}")
print('\n\n')
for _ in range(10):
    die = Die(10)
    print(f"Rolling a {die.sides}-sided die: {die.roll()}")
print('\n\n')
for _ in range(10):
    die = Die(20)
    print(f"Rolling a {die.sides}-sided die: {die.roll()}")