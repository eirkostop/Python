import random

def print_as_string(L):
    result = ''
    for x in L:
        result = result + x
    print(result)

word_bank = ['recursion', 'aggregate','conditional','procedure','function','library','syllabus','modification']
#valid_choices = 'abcdefg'

word = random.choice(word_bank)
secret = []
for i in range(len(word)):
    secret.append('_ ')
guesses = 0

while guesses <= 7 and '_ ' in secret:
    letter = input('Give me a letter: ')
    letter = letter.lower()
    while len(letter) != 1 or not letter.isalpha():
        letter = input('Wrong input! Give me a letter: ')
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                secret[i] = letter
    else:
        guesses = guesses + 1
    print_as_string(secret)

if '_ ' not in secret:
    print('You win!')
else:
    print('You lose!')
