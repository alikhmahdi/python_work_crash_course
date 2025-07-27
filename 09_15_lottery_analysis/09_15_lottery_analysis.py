import random


participants = ('a', 'b', 'c', 'd', 'e', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
for _ in range(10):
    choose_winner = random.sample(participants, 4)
    print("The winners is the person who have this pattern:", choose_winner)