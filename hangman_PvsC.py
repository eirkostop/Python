import random

def print_as_string(L):
    result = ''
    for x in L:
        result = result + x
    print(result)

word_bank = ('laptop', 'algorithm', 'vacations', 'hello', 'programming')
#valid_choices = 'abcdefg'

word = random.choice(word_bank)
secret = []
for i in range(len(word)):
    secret.append('_ ')
guesses = 0

while guesses <= 7 and '_ ' in secret:
    choice = input('Give me a letter: ')
    choice = choice.lower()
    while len(choice) != 1 or not choice.isalpha():
        choice = input('Wrong input! Give me a letter: ')
    if choice in word:
        for i in range(len(word)):
            if word[i] == choice:
                secret[i] = choice
    else:
        guesses = guesses + 1
    print_as_string(secret)

if '_ ' not in secret:
    print('You win!')
else:
    print('You lose!')
