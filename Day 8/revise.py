# Wtite a program to play Rock paper scissors game

import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'
    else:
        return 'You lost!'
def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    
print(play())

#WAP to print pattern

def star(n):
    for i in range(n):
        for j in range(i):
            print('*', end='')
        print('')

    for i in range(n, 0, -1):
        for j in range(i):
            print('*', end='')
        print('')
star(5)


